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

apply_order = InlineKeyboardButton('Взять в работу', callback_data="apply_order")

cancle_order = InlineKeyboardButton('Отменить заказ', callback_data="cancle_order")

def admin_buttons():
    return ReplyKeyboardMarkup(
            [['Изменить курс', 'Заказы'], ['Узнать курс', 'Узнать маржу', 'Статистика'], ['Калькулятор'],['Остановить переписку с юзером']],
            resize_keyboard=True
        )