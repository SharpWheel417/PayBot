from telegram import Update
from telegram.ext import CallbackContext
import os

from src.view.admin.recipt import recipt as aRecipt
from src.view.recipt import recipt as uSendRecipt
from src.model.user import user as u

from src.view.error import error_mess

from src.model.order import order as o
from config import ADMIN

async def handle_document(update: Update, context: CallbackContext):


    order = o.get_active(update.message.chat_id)
    if order is None:
        await error_mess("У вас нет активных заказов", update, context)
        return
    
    if order['timechk'] == "cancle":
        await error_mess("Вы не успели отправить квитанцию, создайте новый заказ", update, context)
        return
    else:

        # Получить файл из обновления
        file = update.message.document

        # Получить имя файла
        file_name = file.file_name


        new_file_path = os.path.join("static/recipt", str(order['ids']) + ".pdf")

        try:
            # Получить файл из Telegram API
            file_obj = await file.get_file()
        except Exception as e:
            await error_mess(str(e), update, context)
            return

        # Сохранить файл на диск с новым именем и путем
        with open(new_file_path, 'wb') as new_file:
            new_file_content = await file_obj.download_as_bytearray()
            new_file.write(new_file_content)

        #Отправляем пользователю сообщение о получении файла
        await uSendRecipt(file_name, update, context)

        await aRecipt(new_file_path, update.effective_user.username, order['ids'], order['sum'], update, context)
        u.state("await_email_url", update.message.chat_id)

        # Отправить сообщение о том, что файл был отправлен
        update.message.reply_text(f'Файл был отправлен пользователю')
