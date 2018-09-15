from chatterbot import ChatBot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
from chatterbot.comparisons import levenshtein_distance

bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    statement_comparison_function=levenshtein_distance,
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
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
    "Response based on answer 'x'. ",
    "y",
    "Response based on answer 'y'. ",
    "z"
    "Z response"
])

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