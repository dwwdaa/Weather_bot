import telebot
from pyowm import OWM
from telebot import types
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('Your API')
mgr = owm.weather_manager()
bot = telebot.TeleBot("Your API")

def find_at(msg):
    for text in msg:
        if 'yes' in text:
            return text

@bot.message_handler(func=lambda msg: msg.text is not None and 'yes' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'OK, send me the name of the city')

def find_at(msg):
    for text in msg:
        if "no" in text:
            return text

@bot.message_handler(func=lambda msg: msg.text is not None and "no" in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'Coded with Python by @Cyber5593')

def find_at(msg):
    for text in msg:
        if "I do not understand your question" in text:
            return text

@bot.message_handler(func=lambda msg: msg.text is not None and "I do not understand your question" in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'I said: Do you want to know the weather anywhere else?')

def find_at(msg):
    for text in msg:
        if "I don't understand your question" in text:
            return text

@bot.message_handler(func=lambda msg: msg.text is not None and "I don't understand your question" in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'I said: Do you want to know the weather anywhere else?')

def find_at(msg):
    for text in msg:
        if "No" in text:
            return text

@bot.message_handler(func=lambda msg: msg.text is not None and "No" in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'Coded with Python by @Cyber5593')

def find_at(msg):
    for text in msg:
        if 'Yes' in text:
            return text

@bot.message_handler(func=lambda msg: msg.text is not None and 'Yes' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, 'OK, send me the name of the city'.format(at_text[1:]))

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.reply_to(message, "Hi, send me the name of the city:")

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.reply_to(message, "If you have problems with the bot, please contact @Cyber5593")

@bot.message_handler(content_types=['text'])
def send_message(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    york = w.temperature('fahrenheit')["temp"]

    bot.reply_to(message, "In " + message.text + " " + str(temp) + "°C" + " or " + str(york) + "°F" + "\n")

    if temp < 10:
        answer = "In " + message.text + " very cold, wear warm clothes"

    elif temp < 20:
        answer = "In " + message.text + " cool/cold, it had better if you wear warm clothes "

    elif temp < 35:
        answer = "The weather is good in " + message.text

    elif temp < 100:
        answer = "In " + message.text + " the weather is too hot, wear whatever you want "

    bot.send_message(message.chat.id, answer)

    bot.reply_to(message, 'Do you want to know the weather anywhere else?')

bot.infinity_polling()