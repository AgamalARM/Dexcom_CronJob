import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

### to view logs on heroku >> https://dashboard.heroku.com/apps/aqueous-crag-15172/logs ####

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print('This cron job is running every 5 minute.')
    print("Tick! The time is: %s" % datetime.now())
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    x = requests.get('https://dexcom-api.herokuapp.com/api/Dexcom_classification', headers=headers)
    y = x.json()
    print(y)


sched.start()
