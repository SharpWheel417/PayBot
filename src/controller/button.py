from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.view.payment import payment
from src.view.no import no
from src.view.yes import yes

async def button_callback(update: Update, context: CallbackContext, *args, **kwargs):
    query = update.callback_query
    # Получаем callback_data из нажатой кнопки
    callback_data = update.callback_query.data

    ##Оплатить покупку или услугу в интернете
    if callback_data == "payment":
        await payment(update, context)

    ##Пользователь выбирает оплату доллорами
    if callback_data == "dollar":
        await payment(update, context)

    ##Пользователь выбирает оплату в евро
    if callback_data == "euro":
        await payment(update, context)

    ##Если пользователь соглашается с заказом и ценой
    if callback_data == "yes":
        await yes(update, context)

    #Если ппользователь оттказывается от заказа
    if callback_data == "no":
        await no(update, context)