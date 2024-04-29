from telegram import Update
from telegram.ext import ContextTypes

### STEP 3 ###

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите сумму в выбранной валюте")

