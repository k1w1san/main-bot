import telebot
import random

token = '6734123120:AAGrCfejtAgRjCv7cCqYIclE0YUUAwVXwQk'
bot = telebot.TeleBot(token)

hello = ['hi', 'hello', "whats up?", 'how are you, boy?']
def filter_password_1(message):
    password = "привет"
    return password in message.text.lower()

def filter_password_2(message):
    password = "пока"
    return password in message.text.lower()

@bot.message_handler(content_types=['text'], func=filter_password_1)
def say_hello(message):
    bot.send_message(message.chat.id, f"{random.choice(hello)}, {message.from_user.username}!")

@bot.message_handler(content_types=['text'], func=filter_password_2)
def say_bye(message):
    bot.send_message(message.chat.id, f"Пока, {message.from_user.username}!")

@bot.message_handler(content_types=['text'])
def repeat(message):
    bot.send_message(message.chat.id, f'Вы написали: {message.text}')

bot.polling()