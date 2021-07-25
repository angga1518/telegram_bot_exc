import logging
from telegram.ext import *
from responses import Responses
API_KEY = '1900563339:AAHAYO6qrQy-EuOV46pVYoSY-cbAg6wWXqY'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')

def start_command(update, context):
    response.reset_message()
    update.message.reply_text('Hello there! I\'m a ROX Profit bot. What\'s up?')
    update.message.reply_text('Please input your item amount and price like this:\namount-price')

def result_command(update, context):
    result = response.get_result()
    if (isinstance(result, float)):
        update.message.reply_text('your profit {}'.format(result))
    else:
        update.message.reply_text(result)


def market_price_command(update, context):
    update.message.reply_text("Please enter market price for the item like this:\nmp-price \nfor example mp-3000")

def quantity_command(update, context):
    update.message.reply_text("please enter quantity you want to sell like this:\nq-quantity \nfor example q-100")

def tax_command(update, context):
    update.message.reply_text("please enter your current text like this:\nt-tax\nfor example t-0.25")

def end_command(update, context):
    response.reset_message()
    update.message.reply_text('Flow ended')
    update.message.reply_text('Please type /start to predict another profit')

def help_command(update, context):
    update.message.reply_text('You can control me by sending these commands: \n/start - predict new profit \n/end - end the current flow\n/h - see commands\n/marketprice - input market price\n/quantity - input quantity \n/tax - input your current tax \n/result : to get your profit result')

def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    return_response = response.get_response(text)
    update.message.reply_text(return_response)

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')

# Run the programme
if __name__ == '__main__':
    response = Responses()

    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('result', result_command))
    dp.add_handler(CommandHandler('marketprice', market_price_command))
    dp.add_handler(CommandHandler('quantity', quantity_command))
    dp.add_handler(CommandHandler('tax', tax_command))
    dp.add_handler(CommandHandler('end', end_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('h', help_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()