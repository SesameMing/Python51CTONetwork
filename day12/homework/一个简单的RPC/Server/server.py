#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-13 20:43
# Version：3.x

import pika
import json
import subprocess

rabbitMQhost = '192.168.199.213'  # rabbitMQ主机地址
severities = ['192.168.199.213']  # 本机ip

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitMQhost))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)
print(' [*] Waiting for logs. To exit press CTRL+C')


def reback(ret, message):

    messagedic = {"ip": severities, "message": message}
    channel.basic_publish(exchange='direct_logs', routing_key=ret, body=json.dumps(messagedic))


def callback(ch, method, properties, body):
    # print(" [x] %r:%r" % (method.routing_key, body))
    ret = json.loads(body.decode())
    print(ret)
    cmd = subprocess.Popen(ret['message'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmd_res = cmd.stdout.read()
    if not cmd_res:
        cmd_res = cmd.stderr.read()
    if len(cmd_res) == 0:  # cmd has mot output
        cmd_res = "没有这个命令"
        # cmd_res = bytes(cmd_res, encoding='utf8')
    reback(ret['requeueu'], cmd_res.decode())

channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()

