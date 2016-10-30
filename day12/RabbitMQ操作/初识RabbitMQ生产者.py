#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 14:56
# Version：3.x
import pika


# ######################### 生产者 #########################
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.199.213'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello world!')
print(" [x] Sent 'Hello World!'")
connection.close()
