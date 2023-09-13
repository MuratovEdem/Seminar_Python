from random import *
import json

def save():
    with open("games.json", "w", encoding="utf-8") as gm:
        gm.write(json.dumps(games,ensure_ascii=False))
    print("Успешно сохранено в файле 'games.json'")

def manual():
    print("Для начала работы бота введите команду '/start', для завершения работы с ботом введите '/stop', для добавления новой игры в сборник введите '/add',")
    print("для удаления игры из сборника '/delete', для вывода на экран всех игр в сборнике '/all', для повторного вызова данного сообщения напишите '/help'")



try:
    games = []
    with open("games.json", "r", encoding="utf-8") as gm:
        games = json.load(gm)
    manual()
except:
    games = []
    games.append("The Wither")
    games.append("The Wither 3 Wild Hunt")
    games.append("Cyberpunk 2077")
    games.append("Red Dead Redemption 2")
    games.append("Rome Total War")
    games.append("Rome Total War 2")
    games.append("Empire Total War")
    games.append("Sid Meier's Civilization VI")
    games.append("The Last of Us")
    games.append("The Last of Us 2")
    manual()

while True:
    command = input("Введите команду: ")
    if command == '/start':
        print("Бот специалист по играм начал свою работу")
    elif command == '/stop':
        print("Бот закончил свою работу")
        break
    elif command == '/add':
        g = input("Введите название игры: ")
        games.append(g)
        print("Игра успешно добавлена в сборник")
    elif command == '/delete':
        g = input("Введите название игры: ")
        try:
            games.remove(g)
            print("Игра успешно удалена из сборника")
        except:
            print("Такой игры в сборнике нет")
    elif command == '/all':
        print("Список игр находящихся в сборнике")
        print(games)
    elif command == '/random':
        print('Случайно выбранная игра это ' + choice(games))
    elif command == '/save':
        save()
    elif command == '/load':
        with open("games.json", "r", encoding="utf-8") as gm:
            games = json.load(gm)
        print("Сборник игр успешно загружен")
    elif command == '/help':
        manual()
    else:
        print('Такое команды нет. Попробуйте снова')