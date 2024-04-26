from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.model.order import close_order

async def no(update: Update, context: ContextTypes.DEFAULT_TYPE):

    close_order(update.effective_user.username)

    txt = mess("no")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)