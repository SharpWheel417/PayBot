# from telegram import Update

# from src.model.order import o

# ##Если проходит фото
# def handle_photo(update: Update, context):

#     order.get_state(update.effective_user.username)

#     # Получить фотографию из обновления
#     photo = update.message.photo[-1]

#     # Получить имя файла фотографии
#     file_name = photo.file_name

#     # Получить файл фотографии
#     file = photo.get_file()

#     # Сохранить файл фотографии на диск
#     file.download(file_name)

#     # Отправить сообщение о том, что фотография была получена
#     update.message.reply_text(f'Фотография "{file_name}" была получена')