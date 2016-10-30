#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 16:39
# Version：3.x
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.199.213'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', type='fanout')
message = ' '.join(sys.argv[1:]) or "info: Hello World"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()