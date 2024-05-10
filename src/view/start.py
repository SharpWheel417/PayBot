from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

# from config import ADMIN
from config import ADMIN
from src.model.data import mess

from src.styles.buttons import admin, buy_button

import src.model.user as user

### Комманда Старт ###
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username
    print(update._effective_chat.id)
    if update.effective_user.last_name is None:
        user_fio = update.effective_user.first_name
    else:
        user_fio = update.effective_user.first_name + " " + update.effective_user.last_name

    ### Админ ###
    if user_id in ADMIN:
        user.add_new_user(user_id, username, user_fio)
        #admin panel
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет админ!", reply_markup=admin.admin_buttons())

    ### Юзер ###
    else:

        ### Добавляем юзера в базу данных ###
        user.add_new_user(user_id, username, user_fio)

        keyboard = InlineKeyboardMarkup([[buy_button]])

        await context.bot.send_message(chat_id=update.effective_chat.id, text=mess("start"))

        await context.bot.send_message(chat_id=update.effective_chat.id, text=mess("start_two"), reply_markup=keyboard)

        # await context.bot.send_message(chat_id=update.effective_chat.id, text=get_message.get_mess('hello_message', False), reply_markup=keyboards.get_user_base())
