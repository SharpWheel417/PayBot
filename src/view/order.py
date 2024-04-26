from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.styles.buttons import yes, no

async def order(summ, update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = InlineKeyboardMarkup([[yes], [no]])
    
    txt = mess("to_pay").format(summ=summ)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt ,reply_markup=keyboard)