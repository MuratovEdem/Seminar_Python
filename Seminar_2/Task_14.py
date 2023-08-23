# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def search_degree_number(number):
    degree_number =[]
    count = 0
    degree = 0
    while degree < number:
        degree_number.append(count)
        count += 1
        degree = 2**count
    print(*degree_number)



try:
    number = int(input("Введите число: "))
    search_degree_number(number)
except:
    print('Введено некорректное значение')