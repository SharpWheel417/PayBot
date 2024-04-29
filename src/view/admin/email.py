from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from config import ADMIN
from src.styles.buttons import admin_order
from src.model.data import mess
from src.model.order import order

## Отправка документа с квитанцией админу
async def email(email, url, update: Update, context: ContextTypes.DEFAULT_TYPE):
  
  o = order.get_active(update.message.chat_id)
  
  txt = mess('came_email_url').format(username = update.effective_user.username,
                                   ids=o['ids'],
                                   sum=o['sum'],
                                   date=o['date'],
                                   email=email,
                                   url=url,
                                   )
  
  for i in ADMIN:
      await context.bot.send_message(chat_id=i, text=txt, reply_markup=admin_order)
      