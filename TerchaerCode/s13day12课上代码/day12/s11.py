# Author:Alex Li
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.11.87'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='kakaxi1', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='kakaxi1',
                      no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()