#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-10-30 18:45
# Version：3.x

import pika
import sys
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.199.213'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')


dic = {"requeueu":"xxxxx","mingling":"xxxxxxxxxxx"}


severity = ['info', 'error']
for severi in severity:

    message = ' '.join(sys.argv[2:]) or json.dumps(dic)
    channel.basic_publish(exchange='direct_logs',
                          routing_key=severi,
                          body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()