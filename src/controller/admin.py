from telegram import Bot, Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler, CallbackContext

from src.view.admin.stats import stats
from model.order import order
from model.user import user
from model.variables import v


def admin_way(text, update: Update, context: ContextTypes.DEFAULT_TYPE):

  ###
  ### Статистика заказов
  ###
  if text == 'Заказы':
    stats.orders(context
                 )
  if text == 'В работе':
    orders = order.in_work()
    stats.orders_print(orders, update, context)

  if text == 'Заявки':
    orders = order.requests()
    stats.orders_print(orders, update, context)

  if text == 'Выполненые':
    orders = order.completes()
    stats.orders_print(orders, update, context)

  if text == 'Отмененные':
    orders = order.cancles()
    stats.orders_print(orders, update, context)

  #################

  ###
  ### Курс
  ###

  if text == 'Курс':
    stats.course(update, context)

  if text == 'Узнать курс':
    stats.check_course(""+v.usd()+" руб.", update, context)

  if text == 'Изменить курс':
    user.state('change_course', update.effective_chat.id)
    stats.change_course(update, context)

### Число
### Админ изменяет курс
###
  if user.get_state(update.effective_chat.id) == 'change_course':
    v.set_usd(float(text))
    stats.check_course("Курс изменен: "+v.usd()+" руб.", update, context)


############# МАРЖА ############


  ###
  ### Админ переходит в меню с маржой
  ###
  if text == 'Маржа':
    stats.marje(update, context)

  ###
  ### Админу выводиться маржа
  ###
  if text == 'Узнать маржу':
    stats.check_marje("Маржа: "+v.marje()+"", context, update)

  ###
  ### Админ хочет изменить маржу
  ###
  if text == 'Изменить маржу':
    user.state('change_marje', update.effective_chat.id)
    stats.change_marje(update, context)

### Число
### Админ изменяет маржу
###
  if user.get_state(update.effective_chat.id) == 'change_marje':
    v.set_marje(float(text)/100)
    stats.check_marje("Марже изменена: "+v.marje()+"", update, context)


  ############ КАЛЬКУЛЯТОР ###############

  # if text == 'Калькулятор':
  #   stats.calculate(update, context)

  # if text == 'Рубль в доллары':

  # if text == 'Доллар в рубль'


  ############# СТАТИСТИКА ########

  if text == 'Статистика':
