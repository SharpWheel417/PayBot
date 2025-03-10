from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.view.admin.stats import stats
from src.model.stats import stats as dbStats
from src.model.order import order
from src.model.user import user
from src.model.variables import v
from src.model.admins import a


async def admin_way(text, update: Update, context: ContextTypes.DEFAULT_TYPE):

  if text == 'Главное меню':
    await stats.main(update, context)

  ###
  ### Статистика заказов
  ###
  if text == 'Заказы':
    await stats.orders_main(update, context)

  if text == 'В работе':
    orders = order.in_work()
    await stats.orders_print(orders, 'active', update, context)

  if text == 'Заявки':
    orders = order.requests()
    await stats.orders_print(orders, 'request', update, context)

  if text == 'Выполненые':
    orders = order.completes()
    await stats.orders_print(orders, 'complete', update, context)

  if text == 'Отмененные':
    orders = order.cancles()
    await stats.orders_print(orders, 'cancle', update, context)

  #################

  ###
  ### Курс
  ###

  if text == 'Курс':
    await stats.course(update, context)

  if text == 'Узнать курс':
    await stats.check_course(""+v.usd()+" руб.", update, context)

### Число
### Админ изменяет курс
###
  if user.get_state(update.effective_chat.id) == 'change_course':
    v.set_usd(float(text))
    await stats.check_course("Курс изменен: "+v.usd()+" руб.", update, context)
    user.state('', update.effective_chat.id)

  if text == 'Изменить курс':
    user.state('change_course', update.effective_chat.id)
    await stats.change_course(update, context)



############# МАРЖА ############


  ###
  ### Админ переходит в меню с маржой
  ###
  if text == 'Маржа':
    await stats.marje(update, context)

  ###
  ### Админу выводиться маржа
  ###
  if text == 'Узнать маржу':
    await stats.check_marje("Маржа: "+v.marje()+"", update, context)

### Число
### Админ изменяет маржу
###
  if user.get_state(update.effective_chat.id) == 'change_marje':
    v.set_marje((float(text)+100)/100)
    await stats.check_marje("Марже изменена: "+v.marje()+"", update, context)
    user.state('', update.effective_chat.id)

  ###
  ### Админ хочет изменить маржу
  ###
  if text == 'Изменить маржу':
    user.state('change_marje', update.effective_chat.id)
    await stats.change_marje(update, context)




  ###
  ### Админ переходит в меню с переменными
  ###
  if text == 'Переменные':
    await stats.vars(update, context)

### Число
### Админ изменяет телефон
###
  if user.get_state(update.effective_chat.id) == 'change_phone':
    v.set_phone(text)
    await stats.check_marje("Телефон изменен: "+v.phone()+"", update, context)
    user.state('', update.effective_chat.id)
  ###
  ### Админу переходит в ввод телефона
  ###
  if text == 'Телефон':
    user.state('change_phone', update.effective_chat.id)
    await stats.check_marje("Введите новый номер телефона", update, context)

  ### Число
### Админ изменяет телефон
###
  if user.get_state(update.effective_chat.id) == 'change_trade_type':
    v.set_trade(text)
    await stats.check_marje("Метод оплаты изменен: "+v.trade_type()+"", update, context)
    user.state('', update.effective_chat.id)

  ###
  ### Админ хочет изменить маржу
  ###
  if text == 'Способ оплаты':
    user.state('change_trade_type', update.effective_chat.id)
    await stats.check_marje("Введите новый способ оплаты", update, context)



  ############ КАЛЬКУЛЯТОР ###############

  if text == 'Калькулятор':
    await stats.calculate(update, context)

  ### STATES ###
  if user.get_state(update.effective_chat.id) == 'rub_to_usd':
    sum =round( float(text) / float(v.usd()), 2)
    await stats.rub_to_usd(sum, update, context)
    user.state('', update.effective_chat.id)

  if user.get_state(update.effective_chat.id) == 'usd_to_rub':
    sum = round( float(text) * float(v.usd()), 2)
    await stats.usd_to_rub(sum, update, context)
    user.state('', update.effective_chat.id)



  if text == 'Рубль в доллары':
    user.state('rub_to_usd', update.effective_chat.id)
    await stats.go_float(update, context)

  if text == 'Доллар в рубль':
    user.state('usd_to_rub', update.effective_chat.id)
    await stats.go_float(update, context)







  ############# СТАТИСТИКА ########

  if text == 'Статистика':
    await stats.statistic(update, context)

  if text == 'Пользователи':
    users = dbStats.all_users()
    await stats.users(users, update, context)

  if text == 'Кол-во выполненых заказов':
    num = dbStats.orders()
    await stats.orders(num, update, context)

  if text == 'Выручка':
    profit = dbStats.all_money()
    await stats.profit(profit, update, context)



  if text == 'Админы':
    await stats.admins(update, context)

  if text == 'Список админов':
    admins = a.get()
    await stats.all_admins(admins, update, context)




### ДОБАВЛЕНИЕ АДМИНА ###
  if user.get_state(update.effective_chat.id) == 'add_admin':
    a.add(text)
    user.state('', update.effective_chat.id)
    await stats.added_admin(text, update, context)

  if text == 'Добавить админа':
    user.state('add_admin', update.effective_chat.id)
    await stats.add_admin(update, context)
##############################



### Удаление АДМИНА ###
  if user.get_state(update.effective_chat.id) == 'delete_admin':
    a.delete(text)
    user.state('', update.effective_chat.id)
    await stats.deleted_admin(text, update, context)

  if text == 'Удалить админа':
    user.state('delete_admin', update.effective_chat.id)
    await stats.add_admin(update, context)
##############################
