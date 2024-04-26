from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext


#Кнопка "Оплатить покупку"
buy_button = InlineKeyboardButton('Оплатить покупку', callback_data="payment")

dollar = InlineKeyboardButton('Сревис принимает оплату в  $', callback_data="dollar")
euro = InlineKeyboardButton('Сревис принимает оплату в €', callback_data="euro")

#Кнопка "Да"
yes = InlineKeyboardButton('Да', callback_data="yes")

#Кнопка "Нет"
no = InlineKeyboardButton('Нет', callback_data="no")