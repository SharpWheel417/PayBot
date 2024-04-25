from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext
import re

from src.model.data import mess

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)

    patternDollar = r"\$"
    patternEuro = r"\€"

    if re.search(patternDollar, text):
        print("Строка заканчивается на доллар")
        summ = int(text.replace("$", ""))
    else:
        if re.search(patternEuro, text):
            print("Строка заканчивается на евро")
            summ = int(text.replace("€", ""))

    result = summ * 1.1

    yes = InlineKeyboardButton('Да', callback_data="yes")
    no = InlineKeyboardButton('Нет', callback_data="no")

    keyboard = InlineKeyboardMarkup([[yes], [no]])

    # txt = "К оплате:"+ str(result)+"₽ с учетом комисси банка и бота. Если совершить оплату сервиса/услуги не удастся, мы совершим возврат средств в полном обьеме. Продолжить?"

    txt = mess("to_pay").format(summ=result)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt ,reply_markup=keyboard)