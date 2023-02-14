import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define a dictionary to store secret codes and verified users
users = {}

# Define a function to handle the start command
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Please enter the secret code to verify your account.')

# Define a function to handle messages containing the secret code
def verify(update, context):
    """Verify the user's account with the secret code."""
    code = update.message.text
    if code in users:
        users[update.message.from_user.id] = True
        update.message.reply_text('Your account has been verified!')
    else:
        update.message.reply_text('Sorry, that code is not valid.')

# Define a function to handle messages from unverified users
def unverified(update, context):
    """Send a message to unverified users."""
    if update.message.from_user.id not in users:
        update.message.reply_text('Sorry, you must be verified to use this bot.')

# Define the main function to run the bot
def main():
    """Start the bot."""
    # Create the Updater and pass in your bot's token
    updater = Updater("5893160347:AAHfrd5QESVn1twJlt8m2kEEOwIhjponk3g", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Add message handlers
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, verify))
    dp.add_handler(MessageHandler(Filters.all, unverified))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

# Call the main function to start the bot
if __name__ == '__main__':
    main()
