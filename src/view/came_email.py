from telegram import Update
from telegram.ext import ContextTypes

from src.model.data import mess

#Отправляем пользователю сообщение о получении файла
async def came_email(update: Update, context: ContextTypes.DEFAULT_TYPE):

    txt = mess("user_came_email")

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)

