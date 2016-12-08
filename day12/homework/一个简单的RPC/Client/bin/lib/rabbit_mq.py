#!/usr/bin/env python
# -*-coding:utf-8-*-
# Author:SemaseMing <blog.v-api.cn>
# Email: admin@v-api.cn
# Time: 2016-11-13 21:33
# Version：3.x
import os
import pika
import sys
import json
from config import setting


class rabbit():

    def __init__(self):
        if os.path.exists(setting.RB_FILE_PATH):
            host = json.load(open(setting.RB_FILE_PATH, 'r'))
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host['rbhost']))
            self.channel = self.connection.channel()
            self.channel.exchange_declare(exchange='direct_logs', type='direct')
        else:
            print("配置文件不存在")

    def sendmsg(self, message, hostlist):
        reque = "serverquer"
        messagedic = {"requeueu": reque, "message": message}
        for severip in hostlist:
            self.channel.basic_publish(exchange='direct_logs', routing_key=severip, body=json.dumps(messagedic))

    def remsg(self, reque, iplist):
        result = self.channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        for i in iplist:
            self.channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=reque)

        def callback(ch, method, properties, body):
            ret = json.loads(body.decode())
            print("%s的回复".center(50, "-") % ret['ip'])
            print(ret['message'])

        self.channel.basic_consume(callback, queue=queue_name, no_ack=True)
        # self.channel.start_consuming()
        self.connection.process_data_events(time_limit=2)


