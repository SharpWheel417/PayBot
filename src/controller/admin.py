from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.view.admin.stats import stats
from src.model.stats import stats as dbStats
from src.model.order import order
from src.model.user import user
from src.model.variables import v


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
    await stats.orders_print(orders, update, context)

  if text == 'Заявки':
    orders = order.requests()
    await stats.orders_print(orders, update, context)

  if text == 'Выполненые':
    orders = order.completes()
    await stats.orders_print(orders, update, context)

  if text == 'Отмененные':
    orders = order.cancles()
    await stats.orders_print(orders, update, context)

  #################

  ###
  ### Курс
  ###

  if text == 'Курс':
    await stats.course(update, context)

  if text == 'Узнать курс':
    await stats.check_course(""+v.usd()+" руб.", update, context)

  if text == 'Изменить курс':
    user.state('change_course', update.effective_chat.id)
    await stats.change_course(update, context)

### Число
### Админ изменяет курс
###
  if user.get_state(update.effective_chat.id) == 'change_course':
    v.set_usd(float(text))
    await stats.check_course("Курс изменен: "+v.usd()+" руб.", update, context)
    user.state('', update.effective_chat.id)


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

  ###
  ### Админ хочет изменить маржу
  ###
  if text == 'Изменить маржу':
    user.state('change_marje', update.effective_chat.id)
    await stats.change_marje(update, context)

### Число
### Админ изменяет маржу
###
  if user.get_state(update.effective_chat.id) == 'change_marje':
    v.set_marje((float(text)+100)/100)
    await stats.check_marje("Марже изменена: "+v.marje()+"", update, context)
    user.state('', update.effective_chat.id)


  ############ КАЛЬКУЛЯТОР ###############

  # if text == 'Калькулятор':
  #   stats.calculate(update, context)

  # if text == 'Рубль в доллары':

  # if text == 'Доллар в рубль'


  ############# СТАТИСТИКА ########

  if text == 'Статистика':
    await stats.statistic(update, context)

  if text == 'Пользователи':
    users = dbStats.all_users()
    await stats.users(users, update, context)

  if text == 'Выполненые':
    num = dbStats.orders()