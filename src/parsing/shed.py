import threading
import schedule
import time

from src.parsing.parse import parsing

lock = threading.Lock()
scheduler_thread = None


def run_scheduler():
    # Запуск шедулера каждый час
    schedule.every(1).minutes.do(lambda: run_with_lock(lambda: parsing(), arg=True))

    # Бесконечный цикл для запуска шедулера
    while True:
        schedule.run_pending()
        time.sleep(10)

def run_with_lock(func):
    with lock:
        func()

# Остановка и завершение предыдущего потока, если он существует
if scheduler_thread is not None:
    scheduler_thread.join()

# Создание и запуск нового потока для шедулера
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()