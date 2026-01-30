import os
from telegram.ext import Updater, MessageHandler, Filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def handle_message(update, context):
    update.message.reply_text("👋 Hi, I'm Roonie. I'm awake and running on Railway.")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
