from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.view.payment import payment
from src.view.no import no
from src.view.yes import yes
from src.view.admin.order import apply_order, cancle_order
from src.view.recipt import u_a_apply_recipt

from src.model.order import order as o
from src.model.user import user as u

async def button_callback(update: Update, context: CallbackContext, *args, **kwargs):
    query = update.callback_query
    # Получаем callback_data из нажатой кнопки
    callback_data = update.callback_query.data

    ##Оплатить покупку или услугу в интернете
    if callback_data == "payment":
        await payment(update, context)

    ##Если пользователь соглашается с заказом и ценой
    if callback_data == "yes":
        await yes(update, context)

    #Если ппользователь оттказывается от заказа
    if callback_data == "no":
        await no(update, context)


    #Админ принимает заказ
    if callback_data == "apply_order":
        await apply_order(update, context)

    #Админ отказывается от заказа
    if callback_data == "cancle_order":
        await cancle_order(update, context)
        
    
    ##Подтверждение квитанции
    if callback_data == "apply_recipt":
        ##Название файла
        file_name = query.message.document.file_name
        ## IDS заказа   
        ids = file_name.split(".pdf")[0]
        ## Обновляем state в БД
        if o.state_order("apply_recipt", ids):
            chat_id = o.chat_id(ids)
            
            u.state('email&url', '', chat_id)
            
            await u_a_apply_recipt(chat_id, update, context)
            
    
            
            
        
    if callback_data == "cancle_recipt":
        print("Отмена заказа")