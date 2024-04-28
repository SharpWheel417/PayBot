from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.view.order import order
from src.model.order import set_order as dbOrder

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    summ = int(text)
    result = summ * 1.1
    if dbOrder(result, update.effective_user.username, update.effective_chat.id, "query"):
        await order(result, update, context)