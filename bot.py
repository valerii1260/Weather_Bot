import telebot
from weather import WeatherPyOwn
import os

bot = telebot.TeleBot(os.environ.get('token_bot__'))

@bot.message_handler(content_types=['text'])
def send_echo(message):
    if message.text.lower() == "погода":
        bot.send_message(message.chat.id, WeatherPyOwn("Харьков", "UA"))


bot.polling(none_stop=True)
