from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from config import ADMIN
from src.styles.buttons import admin_recipt
from src.model.data import mess
from src.model.order import order

## Отправка документа с квитанцией админу
async def recipt(file_path, username:str, ids:str, sum, update: Update, context: ContextTypes.DEFAULT_TYPE):


  txt = mess('came_recipt').format(username = username,
                                   ids=ids,
                                   sum=sum,
                                   )

  for i in ADMIN:
      await context.bot.send_message(chat_id=i, text=txt, reply_markup=admin_recipt)
      # Отправить файл другому пользователю
      await context.bot.send_document(chat_id=i, document=open(file_path, 'rb'))



async def recipt_photo(file_path, username:str, ids:str, sum, update: Update, context: ContextTypes.DEFAULT_TYPE):


  txt = mess('came_recipt').format(username = username,
                                   ids=ids,
                                   sum=sum,
                                   )

  for i in ADMIN:
      await context.bot.send_message(chat_id=i, text=txt, reply_markup=admin_recipt)
      # Отправить файл другому пользователю
      # Sending a photo instead of a document
      with open(file_path, "rb") as photo:
        await context.bot.send_photo(chat_id=i, photo=photo)