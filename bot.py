import telebot
#импортировал инфо полностью, чтобы понимать где какой файл именно из текстового файла(info.), надеюсь такое не считается ошибкой
import random
import info

token = '6734123120:AAGrCfejtAgRjCv7cCqYIclE0YUUAwVXwQk'
bot = telebot.TeleBot(token)
def filter_password_1(message):
    password = "привет"
    return password in message.text.lower()
def filter_password_2(message):
    password = "пока"
    return password in message.text.lower()

#тут я использовал рандом для выбора привета и пока, чтобы было удобнее в info лежит вся текстовая информация а тут она удобно выполняется
@bot.message_handler(content_types=['text'], func=filter_password_1)
def say_hello(message):
    bot.send_message(message.chat.id, f"{random.choice(info.hello_list)}, {message.from_user.username}!")
@bot.message_handler(content_types=['text'], func=filter_password_2)
def say_bye(message):
    bot.send_message(message.chat.id, f"{random.choice(info.bye_list)}, {message.from_user.username}!")
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, '''
        Привет! Я Бот-визитка <Absolute bot>. Я существую для представления различных персонажей.\n
        - /start - активация бота\n
        - /help - список существующих команд''')
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, '''
        Вот список существующих команд бота:
        - /name - представление персонажа\n
        - /age - узнать возраст персонажа\n
        - /race - узнать расу персонажа\n
        - /hobby - увидеть список хобби\n
        - /character_traits - узнать черты характера персонажа\n
        - /skills - узнать навыки и способности персонажа\n
        - /photo - увидеть как я выгляжу :)''')
@bot.message_handler(commands=['name'])
def name_command(message):
    bot.send_message(message.chat.id, info.name_text)
@bot.message_handler(commands=['age'])
def age_command(message):
    bot.send_message(message.chat.id, info.age_text)
@bot.message_handler(commands=['race'])
def race_command(message):
    bot.send_message(message.chat.id, info.race_text)
@bot.message_handler(commands=['hobby'])
def hobby_command(message):
    bot.send_message(message.chat.id, info.hobby_text)
@bot.message_handler(commands=['character_traits'])
def character_traits_command(message):
    bot.send_message(message.chat.id, info.character_traits_text)
@bot.message_handler(commands=['skills'])
def skills_command(message):
    bot.send_message(message.chat.id, info.skills_text)

#тут было легче сразу путь файла сделать, т.к не получилось импортом
@bot.message_handler(commands=['photo'])
def photo_command(message):
    bot.send_message(message.chat.id, 'Я выгляжу так:')
    bot.send_photo(message.chat.id, open('itadori.jpg', 'rb'))

bot.polling()