from telegram import Update, InlineKeyboardButton
from telegram.ext import ContextTypes

from config import ADMIN
from src.styles.buttons import admin
from src.styles.buttons import cancle_order
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

  async def orders_print(self, orders, update: Update, context: ContextTypes.DEFAULT_TYPE):
      ##TODO Сделать красивую отпраку заказов в работе и не забыть про кнопки
      for row in orders:
                order_id, status, date = row
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Order ID: {order_id}, Status: {status}, Date: {date}", reply_markup=InlineKeyboardButton([cancle_order]))

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


 ### СТАТИСТИКА ###

  async def statistic(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="СТатистика: ", reply_markup=admin.stats())

  async def users(self, users, update: Update, context: ContextTypes.DEFAULT_TYPE):
      # for i in users:
      #     await
      ##TODO взять из
      print(users)

  async def orders(self, orders, update: Update, context: ContextTypes.DEFAULT_TYPE):
      for i in orders:
          print(orders)

  async def revenue(self, summ, update: Update, context: ContextTypes.DEFAULT_TYPE):
      await context.bot.send_message(chat_id=update.effective_chat.id, text="Выручка: "+summ+" руб.")

stats = Stats()
