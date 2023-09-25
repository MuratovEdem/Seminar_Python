import json
import telebot
from random import *
import requests

token = '6036568820:AAHkJuXbpyhRWCyjPmCDjb8Xc07UQLx9Q-M'
games = []
tg_bot = telebot.TeleBot(token)

@tg_bot.message_handler(commands=['start'])
def start(message):
    with open("game.json", 'r', encoding="utf-8") as gm:
        games = json.load(gm) 
    tg_bot.send_message(message.chat.id, 'Бот начал работу')



@tg_bot.message_handler(commands=['all'])
def show_all(message):
    try:
        tg_bot.send_message(message.chat.id, 'Вот список игр')
        tg_bot.send_message(message.chat.id, ', '.join(games))
    except:
        tg_bot.send_message(message.chat.id, 'Список игр пуст')

@tg_bot.message_handler(commands=['save'])
def save_all(message):
    with open('game.json', 'w', encoding='utf-8') as gm:
        gm.write(json.dumps(games, ensure_ascii=False))
    tg_bot.send_message(message.chat.id, 'Успешно сохранено')

@tg_bot.message_handler(commands=['add'])
def add_new_game(message):
    new_game = message.text.split()[1:]
    ng = " ".join(new_game)
    games.append(ng)
    tg_bot.send_message(message.chat.id, 'Игра успешно добавлена')

@tg_bot.message_handler(commands=['delete'])
def delete_game(message):
    delete = message.text.split()[1:]
    dt = " ".join(delete)
    try:
        games.remove(dt)
        tg_bot.send_message(message.chat.id, 'Игра успешно удалена')
    except:
        tg_bot.send_message(message.chat.id, 'Такой игры в списке нет')


tg_bot.polling()

