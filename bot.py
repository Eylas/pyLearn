
import telegram
import logging

#bot key: 1670205985:AAGvjk94DEGRvzhBVK5YRKlzH59JtcN73Og
botToken = "1670205985:AAGvjk94DEGRvzhBVK5YRKlzH59JtcN73Og"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

bot = telegram.Bot(token=botToken)
print(bot.get_me())

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

from telegram.ext import Updater
updater = Updater(token=botToken, use_context=True)




updater.start_polling()