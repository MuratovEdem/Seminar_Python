# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8


def search_sequence(list):
    list_new = list.copy()
    temp_list = []
    max_sequence_list = []

    count_temp_list = 0
    while len(list_new) > 0:
        min_index = list_new.index(min(list_new))
        temp_list.append(list_new[min_index])
        list_new.pop(min_index)
        count = 0 
        while count < len(list_new):

            if temp_list[count_temp_list] + 1 == list_new[count]:
                temp_list.append(list_new[count])
                count_temp_list += 1
                list_new.pop(count)
                count = 0
            else:
                count += 1

        if len(temp_list) > len(max_sequence_list):
            max_sequence_list = temp_list.copy()
            temp_list.clear()
            count_temp_list = 0
        else:
            temp_list.clear()
            count_temp_list = 0
    
    return max_sequence_list




list_numbers = [12, 3, 4, 8, 6, 33, 11, 9, 13, 18, 19, 1, 0, 25, 27, 26, 17, 14]
print(f'Заданный список чисел: {list_numbers}')
print(f'Максимальная длина последовательности: {search_sequence(list_numbers)}')
