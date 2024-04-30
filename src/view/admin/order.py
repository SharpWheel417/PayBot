from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext


async def apply_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
  # query = update.callback_query.data
  text = update.callback_query.message.text

  colon_index = text.index(":")
  order_id = text[colon_index + 1:].split("\n")[0].strip()

  print(order_id)



async def cancle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
  text = update.callback_query.message.text

  colon_index = text.index(":")


  order_id = text[colon_index + 1:].strip()


  print(order_id)