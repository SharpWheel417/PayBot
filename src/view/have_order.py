from telegram import Update
from telegram.ext import ContextTypes

from src.model.data import mess

async def have_order(o, update: Update, context: ContextTypes.DEFAULT_TYPE):

    txt = mess('have_order').format(
        date = str(o['date']),
        ids = str(o['ids']))

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)