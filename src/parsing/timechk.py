import threading
import schedule
import time

from datetime import datetime, timedelta

from src.controller.sendmess import sendmess_id
from src.model.order import order

from config import ADMIN


lock = threading.Lock()
scheduler_thread = None


def run_scheduler():
    # Запуск шедулера каждый час
    schedule.every(1).minute.do(lambda: run_with_lock(lambda: time_check(), arg=True))

    # Бесконечный цикл для запуска шедулера
    while True:
        schedule.run_pending()
        time.sleep(10)

def run_with_lock(func, arg):
    with lock:
        func()

# Остановка и завершение предыдущего потока, если он существует
if scheduler_thread is not None:
    scheduler_thread.join()

# Создание и запуск нового потока для шедулера
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()



### Берет все заказы и сравнивает время, если прошло 19 минут, то ставит заказ cancel
def time_check():
    orders = order.get_timechk()

    if orders is not None:
        for o in orders:

            date_str = o[1].strftime("%Y-%m-%d %H:%M:%S")
            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

            updated_date = date_obj + timedelta(minutes=15)

            if datetime.now() >= updated_date:
                order.set_timechk('cancle', o[0])
                id = order.chat_id(o[0])
                #Делаем заказ cancle
                order.status('cancle', o[0])
                sendmess_id(id, 'Заказ отменен, вы не успели отправить квитанцию')
                for i in ADMIN:
                    sendmess_id(i, f"Заказ {o[0]} отменен\nПользователь не успел отправить квитанцию в течении 10 минут")
