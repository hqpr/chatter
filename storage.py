from __future__ import unicode_literals

from chatterbot.output import OutputAdapter


class RabbitMQAdapter(OutputAdapter):
    def process_response(self, statement, session_id=None):
        import pika
        connection = pika.BlockingConnection()
        channel = connection.channel()
        channel.basic_publish(exchange='high',
                              routing_key='high',
                              body=statement.text)
        connection.close()
        print(statement.text)
        return statement.text
