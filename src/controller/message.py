from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.view.order import order as vOrder
from src.model.order import set_order as dbOrder
from src.model.order import order
from src.view.have_order import have_order

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    summ = int(text)
    result = summ * 1.1
    if not order.check_order:
        if dbOrder(result, update.effective_user.username, update.effective_chat.id, "query"):
            await vOrder(result, update, context)

    else:
        o = order.get_active_order(update.effective_user.username)
        await have_order(o, update, context)