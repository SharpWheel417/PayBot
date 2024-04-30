from telegram import Update
from telegram.ext import CallbackContext
import os

from src.view.admin.recipt import recipt as aRecipt
from src.view.recipt import recipt as uSendRecipt
from src.model.user import user as u

from src.model.order import order as o
from config import ADMIN

async def handle_document(update: Update, context: CallbackContext):
    # Получить файл из обновления
    file = update.message.document

    # Получить имя файла
    file_name = file.file_name

    order = o.get_active(update.message.chat_id)

    new_file_path = os.path.join("static/recipt", order['ids'] + ".pdf")

    # Получить файл из Telegram API
    file_obj = await file.get_file()

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
