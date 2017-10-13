from __future__ import unicode_literals

import pika

from chatterbot.conversation import Statement
from chatterbot.input import InputAdapter
from chatterbot.output import OutputAdapter
from chatterbot.utils import input_function


class TestingInputAdapter(InputAdapter):
    def process_input(self, *args, **kwargs):
        import pika

        connection = pika.BlockingConnection()
        channel = connection.channel()

        # Get ten messages and break out
        for method_frame, properties, body in channel.consume('Input'):

            # Display the message parts
            print('[QUESTION] {}'.format(body))

            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)

            # Escape out of the loop after 10 messages
            if method_frame.delivery_tag == 10:
                break
            return Statement(body)

        # Cancel the consumer and return any pending messages
        requeued_messages = channel.cancel()
        print('Requeued %i messages' % requeued_messages)

        # Close the channel and the connection
        channel.close()
        connection.close()

    def process_input_statement(self, *args, **kwargs):
        input_statement = self.process_input(*args, **kwargs)
        return input_statement


class RabbitMQOutputAdapter(OutputAdapter):
    def process_response(self, statement, session_id=None):

        connection = pika.BlockingConnection()
        channel = connection.channel()
        channel.queue_declare(queue='Output')
        channel.basic_publish(exchange='example.text',
                              routing_key='Output',
                              body=statement.text)
        connection.close()
        print('[ANSWER] {}'.format(statement.text))
        return Statement(statement.text)


class RabbitMQInputAdapter(InputAdapter):
    def process_input(self, *args, **kwargs):
        user_input = input_function()

        connection = pika.BlockingConnection()
        channel = connection.channel()
        channel.queue_declare(queue='Input')
        channel.basic_publish(exchange='example.text',
                              routing_key='Input',
                              body=user_input)
        connection.close()
        print('[QUESTION] {}'.format(user_input))
        return Statement(user_input)
