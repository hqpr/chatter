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
    database="database.db"
)

bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.humor",
)

print("Type something to begin...")

while True:
    try:
        bot_input = bot.get_response(None)
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
