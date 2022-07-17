import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime



sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print('This cron job is running every 5 minute.')
    print("Tick! The time is: %s" % datetime.now())
    headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    x = requests.get('https://dexcom-api.herokuapp.com/api/Dexcom_classification', headers=headers1)
    y = x.json()
    print(y)

    # send me this data 
    data =  y
    headers2 = {'Accept': 'Application/json','User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}
#############  'http://dexcom.invasso.com/api/dexcom/reading' ## 'http://127.0.0.1:8000/api/dexcom/reading' ##
    res = requests.post('http://dexcom.invasso.com/api/dexcom/reading', data = data, headers=headers2)
    print("The Response of BackEnd is : ",res.text)


sched.start()
