import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Output')


def callback(ch, method, properties, body):
    print(" [OUTPUT] Received %r" % body)


channel.basic_consume(callback,
                      queue='Output',
                      no_ack=True)

print(' [O] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()