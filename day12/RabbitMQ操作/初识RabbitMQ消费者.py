#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 15:02
# Version：3.x
import pika

# ########################## 消费者 ##########################

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.199.213'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r " % body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages.To exit press CTRL+C')
channel.start_consuming()