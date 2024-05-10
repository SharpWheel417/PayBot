from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.view.order import order as vOrder
from src.model.order import order
from src.view.have_order import have_order
from src.view.came_email import came_email
from src.view.admin.email import email as aEmail
from src.view.payment import my_summ

from config import ADMIN
from src.controller.admin import admin_way

from src.model.variables import v
from src.model.user import user as u

from src.view.error import error_mess

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_regex = r'(https?://[^\s]+)'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    ##Сообщения админа
    if update.effective_chat.id in ADMIN:
        await admin_way(text, update, context)

    else:

        if text == 'Ввести свою сумму':
            await my_summ(update, context)

        ###
        ### Пользователь ввел email и url
        ###
        if u.get_state(update.message.chat_id) == "await_email_url":

            try:
                email = re.search(email_regex, text).group()
                url = re.search(url_regex, text).group()
            except Exception as e:
                print(e)

            try:
                if email and url:
                    if order.email_url(email, url, update.effective_chat.id):
                        await aEmail(email, url, update, context)
                        u.state("await_close_order", update.message.chat_id)
                        await came_email(update, context)
            except Exception as e:
                await error_mess("Вы должны отправить email и ссылку одинм сообщением", update, context)
                

        ########################


        ###
        ### Пользователь ввел сумму
        ###
        else:
            check = order.check(update.effective_chat.id)
            if not check:
                usd = float(v.usd())
                marje = float(v.marje())
                ## Переводим доллары в рубли
                summ = round((int(text) * usd),2)
                ## Плюсуем маржу
                result = round((summ*marje),2)

                ## Вычисляем прибыль
                profit = round((result - summ),2)
                ##Проверяем, есть ли у пользователя активный заказ
                if order.set(result, usd, profit, marje,  update.effective_user.username, update.effective_chat.id, "query"):
                    await vOrder(result, update, context)

            else:
                o = order.get_active(update.message.chat_id)
                await have_order(o, update, context)

        ######################
