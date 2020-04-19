import telebot
from weather import WeatherPyOwn

# print(WeatherPyOwn("Харьков","UA"))

bot = telebot.TeleBot("901291038:AAFRjXLTK8LW0KxyByOlRp-9dCUWJXTRmOk")
flag_w = False


@bot.message_handler(content_types=['text'])
def send_echo(message):
    global flag_w
    if flag_w:
        bot.send_message(message.chat.id, WeatherPyOwn(message.text.lower(), ""))
        flag_w = False
    elif message.text.lower() == "погода":
        flag_w = True
        bot.reply_to(message, "Название города ?")
    else:
        bot.reply_to(message, "Неизвестная команда")


bot.polling(none_stop=True)
