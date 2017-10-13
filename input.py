import pika
import logging

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Input')
logging.basicConfig(level=logging.INFO)


def callback(ch, method, properties, body):
    print(" [INPUT] Received %r" % body)
    logging.debug('[INPUT] Received %r" % body')


channel.basic_consume(callback,
                      queue='Input',
                      no_ack=True)

print(' [I] Waiting for messages. To exit press CTRL+C')
logging.debug(' [I] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
