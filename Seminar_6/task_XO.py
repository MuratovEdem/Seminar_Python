# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
import random

def print_table(list_empty, list_user, list_comp):
    result_table = '\n'
    for i in range(len(list_empty)):
        result_table += print_string(list_empty[i], list_user[i]) + '\n'
    print(result_table)

def print_string(empty, user):
    string_res = '|'
    for i in range(1,4):
        if str(i) in empty:
            string_res += ' |'
        elif str(i) in user:
            string_res += 'x|'
        else:
            string_res += '0|'
    return string_res

def check_for_victory(list_player_move):
    for i in list_player_move:
        if '1' in i and '2' in i and '3' in i:
            return True
    temp_list = ['1', '2', '3']
    for j in temp_list:
        if j in list_player_move[0] and j in list_player_move[1] and j in list_player_move[2]:
            return True
    if '1' in list_player_move[0] and '2' in list_player_move[1] and '3' in list_player_move[2]:
        return True
    if '3' in list_player_move[0] and '2' in list_player_move[1] and '1' in list_player_move[2]:
        return True
    return False

def comp_motion(list_empty: list):
    while True:
        comp_str = random.randint(1,3)
        comp_col = None
        if len(list_empty[comp_str -1]) > 0:
            comp_col = random.choice(list_empty[comp_str -1])
            return str(comp_str), str(comp_col)




list_empty_cells = [['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3']]
list_user_motion = [[], [], []]
list_comp_motion = [[], [], []]

try:
    for i in range(4):
        user_string, user_column = input('Введите номер строки и столбца: ').split()
        list_user_motion[int(user_string)-1].append(user_column)
        list_empty_cells[int(user_string)-1].remove(user_column)
        print_table(list_empty_cells, list_user_motion, list_comp_motion)
        if check_for_victory(list_user_motion):
            print('Вы победили')
            break
        print('Ход бота: \n')
        comp_string, comp_column = comp_motion(list_empty_cells)
        list_comp_motion[int(comp_string)-1].append(comp_column)
        list_empty_cells[int(comp_string)-1].remove(comp_column)
        print_table(list_empty_cells, list_user_motion, list_comp_motion)
        if check_for_victory(list_comp_motion):
            print('Вы проиграли')
            break
    else:
        user_string, user_column = input('Введите номер строки и столбца: ').split()
        list_user_motion[int(user_string)-1].append(user_column)
        list_empty_cells[int(user_string)-1].remove(user_column)
        print_table(list_empty_cells, list_user_motion, list_comp_motion)
        if check_for_victory(list_user_motion):
            print('Вы победили')
        else:
            print('Ничья')
except:
    print('Введено некорректное значение')








