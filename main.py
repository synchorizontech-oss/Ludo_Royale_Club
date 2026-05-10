import os
from fastapi import FastAPI
import telebot
import uvicorn

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Ludo Royale Club backend is running!"}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Ludo Royale Club!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
