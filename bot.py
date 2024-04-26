from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from config import BOT_TOKEN
from src.view.sum import sum
from src.view.handle.message import handle_message
from src.view.payment import payment
from src.view.start import start


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


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CallbackQueryHandler(button_callback))

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT, handle_message)
    application.add_handler(message_handler)


    application.run_polling()
