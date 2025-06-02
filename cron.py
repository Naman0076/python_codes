import schedule
import time
import datetime  
def job():
    now = datetime.datetime.now()
    print("The current time is:", now)

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()