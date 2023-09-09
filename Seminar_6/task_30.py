# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# def get_arithmetic_progress(first: int, step: int, number: int) -> list:
#     list_progression = []
#     for i in range(1, number + 1):
#         list_progression.append(first + (i - 1) * step)
#     return list_progression


first_element = int(input("Введите первый элемент прогрессии: "))
step_progression = int(input("Введите шаг прогрессии: "))
number_elements = int(input("Введите количество элементов: "))

print([(first_element + (i - 1) * step_progression) for i in range(1, number_elements + 1)])
