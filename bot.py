import logging

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# input_adapter='chatterbot.input.TerminalAdapter',
# input_adapter='adapters.RabbitMQInputAdapter',

bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter='adapters.RabbitMQInputAdapter',
    output_adapter='adapters.RabbitMQOutputAdapter',
    database="database.db",
    trainer='chatterbot.trainers.ListTrainer',
)

bot.train([
    "Hi",
    "Hi, can I help you?",
    "Hello",
    "Hi, how can I help you?",
    "file a complain",
    "Against who?",
    "x",
    "Response based on 'X'. ",
    "y",
    "Response based on 'Y'. ",
    "z"
    "Z response"
])

print("Type something to begin...")

while True:
    try:
        bot_input = bot.get_response(None)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
