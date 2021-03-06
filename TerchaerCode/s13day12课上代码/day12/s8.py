# Author:Alex Li
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.11.87'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_fanout',
                         type='fanout')

# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
# 绑定
channel.queue_bind(exchange='logs_fanout',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()