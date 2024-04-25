from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

### STEP 3 ###

### Комманда Старт ###
async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите сумму в выбранной валюте")

