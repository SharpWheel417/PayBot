from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.model.order import yes_order, get_order_code, get_order_sum
from config import ADMIN

async def yes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    yes_order(update.effective_user.username)
    txt = mess("yes")

    ids = get_order_code(update.effective_user.username)
    sum = get_order_sum(update.effective_user.username)

    txt_admin = mess("order_request").format(
        ids=ids,
        username=update.effective_user.username,
        sum=sum,
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
    for i in ADMIN:
        await context.bot.send_message(chat_id=i, text=txt_admin)