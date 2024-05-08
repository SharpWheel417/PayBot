from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.styles.buttons import user_base
from src.model.data import mess

### STEP 2 ###

### Комманда Старт ###
async def error_mess(text, update: Update, context: ContextTypes.DEFAULT_TYPE):

    if text == 'File is too big':
        text = 'Ошика. \n файл слижком большой!'



    await context.bot.send_message(chat_id=update.effective_chat.id, text=str(text), reply_markup=user_base)
