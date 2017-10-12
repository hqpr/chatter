import logging

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# chatbot = ChatBot(
#     'Norman',
#     trainer='chatterbot.trainers.ListTrainer',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     input_adapter='chatterbot.input.TerminalAdapter',
#     output_adapter='chatterbot.output.TerminalAdapter',
#     database='database.sqlite3'
# )
# logic_adapters = [
#                      "chatterbot.logic.MathematicalEvaluation",
#                      "chatterbot.logic.TimeLogicAdapter",
#                      "chatterbot.logic.BestMatch"
#                  ],

# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter='storage.RabbitMQAdapter',
    database="database.db"
)

bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor",
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
