from __future__ import unicode_literals

import pika

from chatterbot.conversation import Statement
from chatterbot.input import InputAdapter
from chatterbot.output import OutputAdapter
from chatterbot.utils import input_function


class RabbitMQOutputAdapter(OutputAdapter):
    def process_response(self, statement, session_id=None):

        connection = pika.BlockingConnection()
        channel = connection.channel()
        channel.queue_declare(queue='Output')
        channel.basic_publish(exchange='',
                              routing_key='Output',
                              body=statement.text)
        connection.close()
        print('[ANSWER] {}'.format(statement.text))
        # self.create_json(statement)
        return statement.text

    def create_json(self, response):
        import json
        data = {
            "message": "",
            "answer": response.text
        }

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)


class RabbitMQInputAdapter(InputAdapter):
    def process_input(self, *args, **kwargs):
        user_input = input_function()

        connection = pika.BlockingConnection()
        channel = connection.channel()
        channel.queue_declare(queue='Input')
        channel.basic_publish(exchange='',
                              routing_key='Input',
                              body=user_input)
        connection.close()
        print('[QUESTION] {}'.format(user_input))
        return Statement(user_input)
