from telegram import Update, InlineKeyboardButton
from telegram.ext import ContextTypes

from config import ADMIN
from src.styles.buttons import admin
from src.styles.buttons import co, admin_first
from src.model.variables import v

class Stats():
  def __init__(self) -> None:
    pass


  async def main(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Главное меню: ", reply_markup=admin.admin_buttons())
    ###
    ### ЗАКАЗЫ
    ###

  async def orders_main(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Заказы: ", reply_markup=admin.orders())

  async def orders_print(self, orders, type, update: Update, context: ContextTypes.DEFAULT_TYPE):

      if type == 'work':
          btn = co
      if type == 'complete':
          btn = ''
      if type == 'request':
          btn = admin_first
      if type == 'cancle':
          btn = ''


      for row in orders:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"ID заказа: {row[8]}\n Суммна: {row[2]}  Date: {row[3]}", reply_markup=btn)

  ########################

###
### Курс
###
  async def course(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Курс: ", reply_markup=admin.course())

###
### Узнать курс
###
  async def check_course(self, course: str,update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=course)

###
### Изменить курс
###
  async def change_course(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите новое значение (в руб.)")



###
### Переменные
###
  async def vars(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Переменные: ", reply_markup=admin.vars())


###
### Маржа
###
  async def marje(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Маржа: ", reply_markup=admin.marje())

###
### Узнать маржу
###
  async def check_marje(self, course: str,update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=course)

###
### Изменить маржу
###
  async def change_marje(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите новое значение (в %)")


  ### КАЛЬКУЛЯТОР ###

  async def calculate(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Калькулятор: ", reply_markup=admin.calculate())

  async def go_float(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Введите число")

  async def rub_to_usd(self, sum, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{sum} $", reply_markup=admin.calculate())

  async def usd_to_rub(self, sum, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{sum} руб.", reply_markup=admin.calculate())


 ### СТАТИСТИКА ###

  async def statistic(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="СТатистика: ", reply_markup=admin.stats())

  async def users(self, users, update: Update, context: ContextTypes.DEFAULT_TYPE):
    messages = []
    message = "Список юзеров:\n"
    for row in users:
        name = str(row[1]).replace(' ', '')
        fio = str(row[4]).replace(' ', '')
        date = str(row[5]).replace(' ', '')
        message += f"@{name} :: {fio} :: {date}\n"
        if len(message) > 3000:  # Пример максимальной длины сообщения
            messages.append(message)
            message = "Список юзеров (продолжение):\n"
    # Добавить последнее сообщение, если оно не пустое
    if message:
        messages.append(message)
    # Отправить сообщения в телеграмм
    for msg in messages:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)




  async def orders(self, orders, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выполнено: "+str(orders))

  async def profit(self, summ, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Выручка: "+str(summ)+" руб.")

stats = Stats()
