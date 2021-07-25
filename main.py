import logging
from telegram.ext import *
import responses

API_KEY = '1900563339:AAHAYO6qrQy-EuOV46pVYoSY-cbAg6wWXqY'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    responses.reset_message()
    update.message.reply_text('Please input your item amount')

def end_command(update, context):
    responses.reset_message()
    update.message.reply_text('Flow ended')
    update.message.reply_text('Please type /start to predict another profit')

def help_command(update, context):
    update.message.reply_text('You can control me by sending these commands: \n /start - predict new profit \n /end end the current flow')

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')

# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('end', start_command))
    dp.add_handler(CommandHandler('help', help_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()