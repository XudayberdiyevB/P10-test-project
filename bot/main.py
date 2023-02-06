import json

import telebot
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    # print(json.loads(message))
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f"Assalomu alaykum, {user.first_name}")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
