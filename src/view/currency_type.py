from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.styles.buttons import dollar, euro
from src.model.data import mess

### STEP 2 ###

### Комманда Старт ###
async def currency_type(update: Update, context: ContextTypes.DEFAULT_TYPE, type):

    if type == "dollar":
      txt = mess("dollar")
    if type == "euro":
      txt = mess("euro")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
