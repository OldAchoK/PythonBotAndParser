import telebot
import requests
import json
import random

bot = telebot.TeleBot('6452738178:AAGWNoBZZpUi1BebQ--N0NGez5GoNd3fV9Q')
isRunning = True

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, "Ну здарова сталкер")
    isRunning = True

@bot.message_handler(commands=['анекдот'])
def anek(message):
    file = open('aneks.json', 'r', encoding="utf-8")
    resp = json.loads(file.read())
    bot.send_message(message.chat.id, resp[f'{random.randint(1, 129)}']['text'])

bot.polling(none_stop=isRunning)

#context.bot.name in [update.message.text[mention.offset:mention.offset + mention.length] for mention in
#                            update.message.entities if mention['type'] == 'mention']