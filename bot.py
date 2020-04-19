import telebot
from weather import WeatherPyOwn

bot = telebot.TeleBot("901291038:AAFRjXLTK8LW0KxyByOlRp-9dCUWJXTRmOk")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    if message.text.lower() == "погода":
        bot.send_message(message.chat.id, WeatherPyOwn("Харьков", "UA"))
    

bot.polling(none_stop=True)
