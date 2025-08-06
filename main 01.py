import json
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

with open("config.json", "r") as f:
    config = json.load(f)

TOKEN = config["8317307798:AAFhi32HH2RjoRPRQsGoKDDAl8BhrOwMpy4"]
CHANNEL_LINK = config["https://t.me/+AndvE0ZgfIxiZWRh"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Enviarei a cobrança Pix em instantes.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
