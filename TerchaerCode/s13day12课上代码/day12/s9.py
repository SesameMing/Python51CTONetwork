# Author:Alex Li
#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.11.87'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_fanout',
                         type='fanout')

message = '456'
channel.basic_publish(exchange='logs_fanout',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()