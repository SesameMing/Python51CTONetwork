# Author:Alex Li
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.11.87'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs_test_1',
                         type='direct')

severity = 'error'
message = '123'
channel.basic_publish(exchange='direct_logs_test_1',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()