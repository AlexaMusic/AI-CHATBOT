import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Set up the chat bot
chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Set up the Telegram bot
TOKEN = '5893160347:AAHfrd5QESVn1twJlt8m2kEEOwIhjponk3g'
bot = telegram.Bot(token=TOKEN)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define the start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm an AI chat bot! Ask me anything.")

# Define the echo command
def echo(update, context):
    message = update.message.text
    response = chatbot.get_response(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(response))

# Set up the Telegram bot handlers
updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Start the bot
updater.start_polling()
updater.idle()
