from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess
from src.model.order import recipt_order, get_order_code, get_order_sum
from src.model.variables import v
from src.styles.buttons import apply_order, cancle_order

from config import ADMIN

async def yes(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #State заказа переводится в recipt (квитанция)
    recipt_order(update.effective_user.username)

    ids = get_order_code(update.effective_user.username)
    sum = get_order_sum(update.effective_user.username)

    txt = mess("yes").format(
        phone=v.phone(),
        trade_type="Сбербанк",
        sum=sum,
        ids=ids
        )


    txt_admin = mess("order_request").format(
        ids=ids,
        username="@"+str(update.effective_user.username),
        sum=sum,
    )

    admin_keyboard = InlineKeyboardMarkup([[apply_order], [cancle_order]])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
    for i in ADMIN:
        await context.bot.send_message(chat_id=i, text=txt_admin, reply_markup=admin_keyboard)