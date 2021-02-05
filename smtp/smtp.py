import http.client
import json
from celery import Celery

# cel = Celery("smtp", broker="pyamqp://guest:guest@localhost//")

# @cel.task(name="smtp.send")


def send(destination, subject, body):
    smtp = http.client.HTTPConnection('127.0.0.1', 8888)
    smtp.request("POST", "/put",
                 json.dumps({
                     'to': destination,
                     'subject': subject,
                     'template': body,
                 }))
    return True
