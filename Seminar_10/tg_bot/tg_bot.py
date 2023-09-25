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



# def save():
#     with open("games.json", "w", encoding="utf-8") as gm:
#         gm.write(json.dumps(games,ensure_ascii=False))
#     print("Успешно сохранено в файле 'games.json'")

# def manual():
#     print("Для начала работы бота введите команду '/start', для завершения работы с ботом введите '/stop', для добавления новой игры в сборник введите '/add',")
#     print("для удаления игры из сборника '/delete', для вывода на экран всех игр в сборнике '/all', для повторного вызова данного сообщения напишите '/help'")



# try:
#     games = []
#     with open("games.json", "r", encoding="utf-8") as gm:
#         games = json.load(gm)
#     manual()
# except:
#     games = []
#     games.append("The Wither")
#     games.append("The Wither 3 Wild Hunt")
#     games.append("Cyberpunk 2077")
#     games.append("Red Dead Redemption 2")
#     games.append("Rome Total War")
#     games.append("Rome Total War 2")
#     games.append("Empire Total War")
#     games.append("Sid Meier's Civilization VI")
#     games.append("The Last of Us")
#     games.append("The Last of Us 2")
#     manual()

# while True:
#     command = input("Введите команду: ")
#     if command == '/start':
#         print("Бот специалист по играм начал свою работу")
#     elif command == '/stop':
#         print("Бот закончил свою работу")
#         break
#     elif command == '/add':
#         g = input("Введите название игры: ")
#         games.append(g)
#         print("Игра успешно добавлена в сборник")
#     elif command == '/delete':
#         g = input("Введите название игры: ")
#         try:
#             games.remove(g)
#             print("Игра успешно удалена из сборника")
#         except:
#             print("Такой игры в сборнике нет")
#     elif command == '/all':
#         print("Список игр находящихся в сборнике")
#         print(games)
#     elif command == '/random':
#         print('Случайно выбранная игра это ' + choice(games))
#     elif command == '/save':
#         save()
#     elif command == '/load':
#         with open("games.json", "r", encoding="utf-8") as gm:
#             games = json.load(gm)
#         print("Сборник игр успешно загружен")
#     elif command == '/help':
#         manual()
#     else:
#         print('Такое команды нет. Попробуйте снова')