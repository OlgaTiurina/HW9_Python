from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from menu.menuPai import *

bot = Bot(token = '5603880098:AAH8N3PibSyQkSCOt4-WfBtFTf1_i8EzPcA')
updater = Updater(token = '5603880098:AAH8N3PibSyQkSCOt4-WfBtFTf1_i8EzPcA')
dispatcher = updater.dispatcher

start_handler = CommandHandler("Hello", start)
abv_handler = MessageHandler(Filters.text, abv)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(abv_handler)

updater.start_polling()
updater.idle()