import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

# Set up the logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the chatbot
chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Define a function to handle incoming messages
def handle_message(update, context):
    text = update.message.text
    response = chatbot.get_response(text)
    update.message.reply_text(str(response))

# Define a function to start the bot
def start_bot():
    # Set up the Telegram API and get the bot's token
    token = "5893160347:AAHfrd5QESVn1twJlt8m2kEEOwIhjponk3g"
    bot = telegram.Bot(token)
    updater = Updater(token, use_context=True)

    # Set up the command handler for the /start command
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Set up the message handler to handle incoming messages
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    logger.info("Bot started.")

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Hello! I am a chatbot. How can I help you today?')

start_bot()
