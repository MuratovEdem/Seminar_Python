# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех команд.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Пример входа:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Выход будет:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


def get_invoice_table(input_data: list):
    all_game_list_in_list = []
    for i in input_data:
        all_game_list_in_list.append(i.split(';'))
    all_commands = get_total_team(all_game_list_in_list)
    result_dict = dict.fromkeys(all_commands, [])
    result_dict = calc_current_points(all_commands, all_game_list_in_list,result_dict)
    print_invoice_table(result_dict)

def get_total_team(game_list: list) -> set:
    commangs_list = []
    for i in game_list:
        for j in range(len(i)):
            if j == 0 or j == 2:
                commangs_list.append(i[j])
    commands_set = set(commangs_list)
    return commands_set

def calc_current_points(commands: set, all_game: list, res_dict: dict) -> dict:
    for i in commands:
        game_count = 0
        win_count = 0
        lose_count = 0
        draw_count = 0
        point_count = 0
        for j in all_game:
            if i in j:
                game_count += 1
                if j.index(i) == 0:
                    if int(j[1]) > int(j[-1]):
                        win_count += 1
                        point_count += 3
                    elif int(j[1]) < int(j[-1]):
                        lose_count += 1
                    else:
                        draw_count += 1
                        point_count += 1
                else:
                    if int(j[-1]) > int(j[1]):
                        win_count += 1
                        point_count += 3
                    elif int(j[-1]) < int(j[1]):
                        lose_count += 1
                    else:
                        draw_count += 1
                        point_count += 3
        res_dict[i] = res_dict.get(i, []) + [game_count] + [win_count] + [draw_count] + [lose_count] + [point_count]
    return res_dict

def print_invoice_table(table_dict: dict):
    for key, value in table_dict.items():
        print(key, ':', *value)




input_data_list = ['Спартак;9;Зенит;10', 'Локомотив;12;Зенит;3', 'Спартак;8;Локомотив;15']

# total_game = int(input("Введите количество игр: "))
# input_data_list = []
# for i in range(1, total_game +1):
#     input_data_list.append(input(f'Игра №{i}: '))

get_invoice_table(input_data_list)