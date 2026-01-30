import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.environ["BOT_TOKEN"]

def reply(update, context):
    update.message.reply_text("Roonie is alive on Railway.")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
