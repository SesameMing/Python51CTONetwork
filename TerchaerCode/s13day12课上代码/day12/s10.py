# Author:Alex Li
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.11.87'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='kakaxi1', durable=True)

channel.basic_publish(exchange='',
                      routing_key='kakaxi1',
                      body='{"cmd": "ls", "queue_name": "asdfasdfjaisjdf"}',
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()