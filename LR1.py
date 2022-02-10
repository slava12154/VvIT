import telebot
from telebot import types

token = ""

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])

def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('aboba','/help')
    bot.send_message(message.chat.id, 'Привет! Я бот, не трогай меня.', reply_markup = keyboard)

@bot.message_handler(commands=['help'])

def start_message(message):
    bot.send_message(message.chat.id, 'Я умею ничего не делать, отстань от меня. \n /disturb - побеспокоить бота')
    

@bot.message_handler(commands=['disturb'])

def answer(message):
    bot.send_message(message.chat.id,'Отстань от меня, я ничего не буду для тебя делать.')

@bot.message_handler(content_types=['text'])

def answer(message):
    if (message.text.lower() == 'aboba'):
        bot.send_message(message.chat.id,'Отстань от меня, зумер.')
        
    elif (message.text.lower() == 'почему ты такой злой?'):
         bot.send_message(message.chat.id,'Я не злой, я пассивно агрессивный.')
            
    else:
        bot.send_message(message.chat.id,'Отстань от меня, я тебя не понимаю.')

bot.infinity_polling()
