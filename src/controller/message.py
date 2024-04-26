from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.view.order import order
from src.model.order import order as dbOrder

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text


    patternDollar = r"\$"
    patternEuro = r"\€"
    type=""
    if re.search(patternDollar, text):
        print("Строка заканчивается на доллар")
        summ = int(text.replace("$", ""))
        type="dollar"
        result = summ * 1.1
        if dbOrder(result, type, update.effective_user.username, update.effective_chat.id, "query"):
            await order(result, update, context)
    else:
        if re.search(patternEuro, text):
            print("Строка заканчивается на евро")
            summ = int(text.replace("€", ""))
            type="euro"
            result = summ * 1.1
            if dbOrder(result, type, update.effective_user.username, update.effective_chat.id, "query"):
                await order(result, update, context)
        