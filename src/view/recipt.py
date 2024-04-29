from telegram import Update
from telegram.ext import ContextTypes

from src.model.data import mess

#Отправляем пользователю сообщение о получении файла
async def recipt(file_name, update: Update, context: ContextTypes.DEFAULT_TYPE):

    txt = mess("user_send_recipt").format(file_name = file_name)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
    
    
async def u_a_apply_recipt(chat_id, update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await context.bot.sendPhoto(chat_id=int(chat_id), photo=open("static/img/screen.jpg", 'rb'))
    
    await context.bot.send_message(chat_id=int(chat_id), text=mess('u_a_apply_recipt'))
