from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from . import task


def start():
    scheduler = BackgroundScheduler()
    
    # scheduler.add_job(task.hello, 'interval', seconds=5)

    scheduler.add_job(task.hello, 'cron', hour=17, minute=5)

    scheduler.start()