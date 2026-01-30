import os
import google.generativeai as genai
from telegram.ext import Updater, MessageHandler, Filters

# Required environment variables
TOKEN = os.environ["BOT_TOKEN"]
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_KEY:
    raise RuntimeError("GEMINI_API_KEY is not set in Railway variables")

# Configure Gemini with your API key
genai.configure(api_key=GEMINI_KEY)

# Use a free Gemini model
model = genai.GenerativeModel("gemini-pro")

def reply(update, context):
    user_text = update.message.text

    prompt = f"""
You are a personal assistant called Roonie.
Reply naturally and helpfully to the user.

User message: {user_text}
"""

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
    except Exception as e:
        text = f"Gemini error: {e}"

    update.message.reply_text(text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
