from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.model.order import order
from src.model.data import mess
from src.model.variables import v


async def apply_order(update: Update, context: ContextTypes.DEFAULT_TYPE):

  text = update.callback_query.message.text

  colon_index = text.index(":")
  ids = text[colon_index + 1:].split("\n")[0].strip()

  sum = order.get_sum(ids)

  txt = mess("yes").format(
      phone=v.phone(),
      trade_type=v.trade_type(),
      sum=sum,
      ids=ids
      )

  chat_id = order.chat_id(ids)

  await context.bot.send_message(chat_id=chat_id, text=txt)

  await context.bot.send_message(chat_id=update.effective_chat.id, text='Заказ взят в работу')



async def cancle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(chat_id=update.effective_chat.id, text='Заказ отменен')