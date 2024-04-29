from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext


#Кнопка "Оплатить покупку"
buy_button = InlineKeyboardButton('Оплатить покупку', callback_data="payment")

#Кнопка "Да"
yes = InlineKeyboardButton('Да', callback_data="yes")

#Кнопка "Нет"
no = InlineKeyboardButton('Нет', callback_data="no")

apply_order = InlineKeyboardButton('Взять в работу', callback_data="apply_order")

cancle_order = InlineKeyboardButton('Отменить заказ', callback_data="cancle_order")

admin_first = InlineKeyboardMarkup([[apply_order], [cancle_order]])

#Когда бот присылает админу квитанцию
apply_recipt = InlineKeyboardButton('Принять квитанцию', callback_data="apply_recipt")
cancle_recipt = InlineKeyboardButton('Отменить квитанцию', callback_data="cancle_recipt")
admin_recipt = InlineKeyboardMarkup([[apply_recipt], [cancle_recipt]])


complete_order = InlineKeyboardButton('Заказ выполнен', callback_data="complete_order")
error_order = InlineKeyboardButton('Не получилось выполнить заказ', callback_data="error_order")
admin_order = InlineKeyboardMarkup([[complete_order], [error_order]])


def admin_buttons():
    return ReplyKeyboardMarkup(
            [['Изменить курс', 'Заказы'], ['Узнать курс', 'Узнать маржу', 'Статистика'], ['Калькулятор'],['Остановить переписку с юзером']],
            resize_keyboard=True
        )