import schedule
import threading
import time

from src.model.order import order

from src.view.comfrim_sum import yes

def print_orders():
    order.where_status("await")

def run_scheduled_jobs():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule the job to run every day at 10 AM
schedule.every().day.at("10:00").do(job)

# Start the scheduled jobs in a separate thread
thread = threading.Thread(target=run_scheduled_jobs)
thread.start()