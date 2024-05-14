from telegram import Update
from telegram.ext import CallbackContext
import os
import requests

from src.view.admin.recipt import recipt_photo as aRecipt_photo
from src.view.recipt import recipt as uSendRecipt
from src.model.user import user as u

from src.view.error import error_mess

from src.model.order import order as o
from config import ADMIN

async def handle_photo(update: Update, context: CallbackContext):
  '''
  Обрабатывает приходящие фотографии
  '''

  order = o.get_active(update.message.chat_id)
  if order is None:
        await error_mess("У вас нет активных заказов", update, context)
        return

  if order['timechk'] == "cancle":
        await error_mess("Вы не успели отправить квитанцию, создайте новый заказ", update, context)
        return
  else:

        # Получить фото из обновления
        photo_file = update.message.photo[-1]
        file_obj = await photo_file.get_file()


        # Сохранить файл на диск с новым именем и путем
        new_file_path = os.path.join("static/recipt/photo", str(order['ids']) + ".jpg")

        # Получить файл как массив байтов
        file_content = await file_obj.download_as_bytearray()

    # Сохранить файл на диск
        with open(new_file_path, 'wb') as new_file:
          new_file.write(file_content)


        # except Exception as e:
        #   await error_mess(str(e), update, context)
        #   return

        # Отправить фотографию админу

        await aRecipt_photo(new_file_path, update.effective_user.username, order['ids'], order['sum'], update, context)


        #Отправляем пользователю сообщение о получении файла
        await uSendRecipt("Фотография", update, context)

        # Отправить сообщение о том, что файл был отправлен
        update.message.reply_text(f'Файл был отправлен пользователю')

        o.set_timechk('complete', order['ids'])
