import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction
import openai

# Set up OpenAI API
openai.api_key = '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'

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a function to start the bot
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm an AI chatbot. Send me a message and I'll try to respond with something intelligent.")

# Define a function to handle text messages
def handle_message(update, context):
    # Send typing action to show the bot is processing
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    
    # Get the message text
    message_text = update.message.text
    
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        engine='davinci',
        prompt=message_text,
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Send the response to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Set up the Telegram bot
def main():
    # Create an Updater object
    updater = Updater(token='5893160347:AAHfrd5QESVn1twJlt8m2kEEOwIhjponk3g', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))

    # Add message handler
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    # Start the bot
    updater.start_polling()
    logging.info('Telegram AI bot started. Press Ctrl+C to stop.')
    updater.idle()

if __name__ == '__main__':
    main()
