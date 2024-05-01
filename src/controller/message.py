from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.view.order import order as vOrder
from src.model.order import order
from src.view.have_order import have_order
from src.view.came_email import came_email
from src.view.admin.email import email as aEmail

from src.model.variables import v
from src.model.user import user as u

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_regex = r'(https?://[^\s]+)'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    ###
    ### Пользователь ввел email и url
    ###
    if u.get_state(update.message.chat_id) == "await_email_url":
        
        try:
            email = re.search(email_regex, text).group()
            url = re.search(url_regex, text).group()
        except Exception as e:
            print(e)

        if email and url:
            if order.email_url(email, url, update.effective_chat.id):
                await aEmail(email, url, update, context)
                u.state("await_close_order", update.message.chat_id)
                await came_email(update, context)
    
    ########################
        
        
    ###
    ### Пользователь ввел сумму
    ###
    else:
        usd = float(v.usd())
        marje = float(v.marje())
        ## Переводим доллары в рубли
        summ = round((int(text) * usd),2)
        ## Плюсуем маржу
        result = round((summ*marje),2)

        ## Вычисляем прибыль
        profit = round((result - summ),2)
        ##Проверяем, есть ли у пользователя активный заказ
        check = order.check(update.effective_chat.id)
        if not check:
            if order.set(result, usd, profit, marje,  update.effective_user.username, update.effective_chat.id, "query"):
                await vOrder(result, update, context)

        else:
            o = order.get_active(update.message.chat_id)
            await have_order(o, update, context)
            
    ######################
        
        