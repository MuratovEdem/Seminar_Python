# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import randint

def get_index_number(min_number: int, max_number: int) -> list:
    print(list_numbers := [randint(1,300) for _ in range(10)])
    print([list_numbers.index(x) for x in list_numbers if min_element < x < max_element])


min_element = 33
max_element = 200

get_index_number(min_element, max_element)