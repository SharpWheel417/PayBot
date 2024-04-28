from telegram import Update
from telegram.ext import CallbackContext
import os

from src.model.order import order as o
from config import ADMIN

async def handle_document(update: Update, context: CallbackContext):
    # Получить файл из обновления
    file = update.message.document

    # Получить имя файла
    file_name = file.file_name

    order = o.get_active_order(update.effective_user.username)

    new_file_path = os.path.join("static/recipt", order['ids'] + ".pdf")

    # Получить файл из Telegram API
    file_obj = await file.get_file()

    # Сохранить файл на диск с новым именем и путем
    with open(new_file_path, 'wb') as new_file:
        new_file_content = await file_obj.download_as_bytearray()
        new_file.write(new_file_content)

    # Отправить сообщение о том, что файл был получен
    update.message.reply_text(f'Файл "{file_name}" был получен')


    for i in ADMIN:
      # Отправить файл другому пользователю
      await context.bot.send_document(chat_id=i, document=open(new_file_path, 'rb'))

    # Отправить сообщение о том, что файл был отправлен
    update.message.reply_text(f'Файл был отправлен пользователю')
