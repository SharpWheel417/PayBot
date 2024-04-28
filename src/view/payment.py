from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext


from src.model.data import mess

### STEP 2 ###

### Комманда Старт ###
async def payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    txt = mess("info")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
