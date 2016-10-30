#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 17:02
# Version：3.x
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.199.213'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs, To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()