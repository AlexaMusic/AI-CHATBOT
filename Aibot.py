import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the OpenAI API key
openai.api_key = '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'

# Define the message handler function
def chat(update, context):
    # Get the user's input
    user_input = update.message.text

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci", prompt=user_input, max_tokens=1024, n=1, stop=None, temperature=0.5
    )
    bot_response = response.choices[0].text

    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_response)

# Set up the bot
updater = Updater('5893160347:AAHfrd5QESVn1twJlt8m2kEEOwIhjponk3g', use_context=True)

# Add the message handler to the bot
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

# Start the bot
updater.start_polling()
updater.idle()
