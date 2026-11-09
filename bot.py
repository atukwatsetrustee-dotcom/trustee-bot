import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm alive. Send me any message and I'll reply.")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"You said: {text}")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("Bot is running...")
    app.run_polling()

# Fake web server so Render doesn't sleep
web = Flask(__name__)
@web.route('/')
def home():
    return "Bot is alive!"

threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
