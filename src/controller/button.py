from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from datetime import datetime, time


import re

from src.view.payment import payment
from src.view.comfrim_sum import no, yes
from src.view.admin.order import apply_order, cancle_order
from src.view.admin.order import cancle_order as admin_cancel_order
from src.model.order import close_order, recipt_order, get_order_ids, get_order_sum
from src.view.recipt import u_a_apply_recipt, u_a_cancle_recipt
from src.view.order import complete_order, error_order, cancle_order
from src.view.order import cancle_order as u_cancle_order

from src.model.order import order as o
from src.model.user import user as u

async def button_callback(update: Update, context: CallbackContext, *args, **kwargs):

    pattern = r"ID заказа: \b[A-Fa-f0-9-]+\b"

    query = update.callback_query
    # Получаем callback_data из нажатой кнопки
    callback_data = update.callback_query.data

    ##Оплатить покупку или услугу в интернете
    if callback_data == "payment":
        u.state('await_sum', update.effective_chat.id)
        await payment(update, context)

    ##Если пользователь соглашается с заказом и ценой
    if callback_data == "yes":
        #State заказа переводится в recipt (квитанция)
        recipt_order(update.effective_chat.id, 'request')
        ids = get_order_ids(update.effective_chat.id)
        sum = get_order_sum(update.effective_chat.id)
        await remove_buttons(update, context)
        await yes(ids, sum, update, context)

    #Если ппользователь оттказывается от заказа
    if callback_data == "no":
        close_order(update.effective_chat.id)
        await remove_buttons(update, context)
        await no(update, context)


    #Админ принимает заказ
    if callback_data == "apply_order":
        # Удалить кнопки после обработки
        await remove_buttons(update, context)
        text = update.callback_query.message.text

        colon_index = text.index(":")
        order_id = text[colon_index + 1:].split("\n")[0].strip()

        o.state('await_recipt', order_id)
        u.state('await_recipt', update.effective_chat.id)
        o.status('active', order_id)
        o.set_time(order_id)

        await apply_order(update, context)

    #Админ отказывается от заказа
    if callback_data == "cancle_order":
        text = update.callback_query.message.text
        ids = re.search(pattern, text).group()
        ids = ids.replace("ID заказа: ", "")
        chat_id = o.chat_id(ids)
        # Удалить кнопки после обработки
        o.status('cancle', ids)
        o.state('cancle', ids)
        o.set_timechk('cancle', ids)
        await admin_cancel_order(update, context)
        #Сообщение об отмене заказа для пользователя
        await u_cancle_order(chat_id, update, context)
        await remove_buttons(update, context)


    ##Подтверждение квитанции
    if callback_data == "apply_recipt":

        text = query.message.text
        ids = re.search(pattern, text).group()
        ids = ids.replace("ID заказа: ", "")

        ## Обновляем state в БД
        if o.state("apply_recipt", ids):
            chat_id = o.chat_id(ids)

            u.state('await_email_url', chat_id)
            # Удалить кнопки после обработки
            await remove_buttons(update, context)

            await u_a_apply_recipt(chat_id, update, context)

        ##Отмена квитанции
    if callback_data == "cancle_recipt":
        ##Название файла
        file_name = query.message.document.file_name
        ## IDS заказа
        ids = file_name.split(".pdf")[0]
        if o.state('cancle_recipt', ids):
            o.status('cancle', ids)
            chat_id = o.chat_id(ids)
            u.state('await_sum', chat_id)
            await u_a_cancle_recipt(chat_id, update, context)
            # Удалить кнопки после обработки
            await remove_buttons(update, context)



    ## Заказ выполнен
    if callback_data == "complete_order":

        ##Находим ids заказа в сообщении
        text = query.message.text
        ids = re.search(pattern, text).group()
        ids = ids.replace("ID заказа: ", "")

        #Получаем chat_id заказчика
        chat_id = o.chat_id(ids)

        # Меняем статусы заказа на complete
        u.state('order_complete', chat_id)
        o.state('order_complete', ids)
        o.status('complete', ids)

        # Отправляем сообщение пользователю о завершенном заказе
        await complete_order(chat_id, update, context)

        # Удалить кнопки после обработки
        await remove_buttons(update, context)


    if callback_data == "error_order":

        ##Находим ids заказа в сообщении
        text = query.message.text
        ids = re.search(pattern, text).group()
        ids = ids.replace("ID заказа: ", "")

        #Получаем chat_id заказчика
        chat_id = o.chat_id(ids)

         # Меняем статусы заказа на complete
        u.state('order_cancle', chat_id)
        o.state('order_cancle', ids)
        o.status('cancle', ids)

        # Отправляем сообщение пользователю о завершенном заказе
        await error_order(chat_id, update, context)

        # Удалить кнопки после обработки
        await remove_buttons(update, context)




# Удаление кнопок из сообщения
# Удаление кнопок из сообщения
async def remove_buttons(update, context):
    await context.bot.edit_message_reply_markup(chat_id=update.effective_chat.id,
                                                message_id=update.effective_message.message_id,
                                                reply_markup=InlineKeyboardMarkup([]))
