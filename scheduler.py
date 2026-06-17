import schedule
import time

def job():
    print("Scheduled Task Executed!")

def start_scheduler():
    schedule.every(10).seconds.do(job)

    print("\nScheduler Started...")

    for _ in range(3):
        schedule.run_pending()
        time.sleep(10)