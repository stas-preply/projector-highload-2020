from __future__ import print_function

import datetime
import random
import string

import beanstalkc
import redis
from flask import Flask

app = Flask(__name__)
app.debug = True

redis_queue = redis.Redis(host='redis', port=6379)

try:
    beanstalk_queue = beanstalkc.Connection(host='beanstalkd', port=11300)
except beanstalkc.SocketError:
    pass


def get_message(
        counter_,
        # size=8 * 1024 * 512     # 512 kb
        size=8 * 1024 * 63     # 63 kb
):
    message = '{}:::{}:::'.format(counter_, datetime.datetime.now())
    if size:
        extra_size = size - len(message) * 8
        text_length = extra_size // 8
        text = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(text_length)
        )
        message += text
    return message


def publish_beanstalkd(counter_):
    message = get_message(counter_)
    beanstalk_queue.put(message)
    return message


def publish_redis(counter_):
    message = get_message(counter_)
    redis_queue.rpush('QUEUE', message)
    return message


# Uncomment the line below according to the queue you want to use

# publish = publish_beanstalkd
publish = publish_redis


counter = 0


@app.route('/')
def hello():
    global counter
    message = publish(counter)
    response = 'Message was published: {}'.format(':::'.join(message.split(':::')[:2]))
    counter += 1
    return response
