from flask import Flask
from celery import Celery
import time
import random

from datetime import datetime

application = Flask(__name__)
application.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
application.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

client = Celery("redisdemo", broker=application.config['CELERY_BROKER_URL'])
client.conf.update(application.config)

@application.route("/")
def home():
    print("submit task at ", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    sampletask.delay("first")
    print("finished submitting task at ", datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
    return "home page"

@client.task()
def sampletask(name):
    print(f"task begins {name}...")
    t = random.randint(1, 10)
    time.sleep(t)
    print(f"task completed, took {t} seconds!\n")


if __name__ == "__main__":
    application.run()
