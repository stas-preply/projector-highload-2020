import datetime
from dateutil.parser import parse

import beanstalkc
import redis

redis_queue = redis.Redis(host='redis', port=6379)

try:
    beanstalk_queue = beanstalkc.Connection(host='beanstalkd', port=11300)
except beanstalkc.SocketError:
    pass


def get_data(text):
    counter_, message, text = text.split(':::')
    return counter_, message


def receive_beanstalkd():
    counter_, message = None, None
    job = beanstalk_queue.reserve()
    if job is not None:
        counter_, message = get_data(job.body)
        job.delete()
    return int(counter_), parse(message)


def receive_redis():
    counter_, message = None, None
    data = redis_queue.rpop('QUEUE')
    if data is not None:
        counter_, message = get_data(data)
        counter_ = int(counter_)
        message = parse(message)
    return counter_, message


# Uncomment the line below according to the queue you want to use

# receive = receive_beanstalkd
receive = receive_redis


def output(*args):
    print('\t'.join(str(arg) for arg in args))


def listen():
    counter = 0
    while True:
        message_counter, message_time = receive()
        if not all([message_counter, message_time]):
            continue
        now = datetime.datetime.now()
        if message_time:
            delta_time = now - message_time
            delta_counter = counter - message_counter
            output(message_counter, message_time, counter, now, delta_time, delta_counter)
            counter += 1


if __name__ == '__main__':
    listen()
