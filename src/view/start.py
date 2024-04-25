from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.view.payment import payment

### Комманда Старт ###
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global user_course_rub, user_course_THB
    user_id = update.effective_user.id
    username = update.effective_user.username
    print(update._effective_chat.id)
    if update.effective_user.last_name is None:
        user_fio = update.effective_user.first_name
    else:
        user_fio = update.effective_user.first_name + " " + update.effective_user.last_name

    # db.add_new_user(user_id, username, user_fio)

    # s.set_state(user_id, '0')
    # db.set_bats(user_id, '0')

    ### Админ ###
    # if user_id in ADMIN_ID:
    #     #admin panel
    #     await context.bot.send_message(chat_id=update.effective_chat.id, text=get_message.get_mess("hello_message", True), reply_markup=keyboards.get_admin_base())

    ### Юзер ###
    # else:
        
        buy_button = InlineKeyboardButton('Оплатить покупку', callback_data="payment")

        keyboard = InlineKeyboardMarkup([[buy_button]])

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте!  Данный бот создан @Mar1osh.\nЕсли у вас возникли какие-либо вопросы, ошибки в работе бота или вам нужна дополнительная услуга, то пишите мне в личные сообщения с тегом #Оплата_через_бота.")

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Мы проводим оплаты ежедневно с 8:00 МСК по 20:00 МСК. Если вы начали работу с ботом до конца рабочего дня, но не успели воспользоваться его услугами, то бот продолжает для вас работу. Если бот не получает сообщений от вас в течении 10 минут, то он закрывает заказ.", reply_markup=keyboard)

        # await context.bot.send_message(chat_id=update.effective_chat.id, text=get_message.get_mess('hello_message', False), reply_markup=keyboards.get_user_base())

