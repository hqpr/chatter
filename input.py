import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Input')


def callback(ch, method, properties, body):
    print(" [INPUT] Received %r" % body)


channel.basic_consume(callback,
                      queue='Input',
                      no_ack=True)

print(' [I] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
