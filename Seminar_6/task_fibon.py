# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def get_megafibon(number):
    list_fibon = [-1, 0, 1]
    for i in range(number-1):
        temp = list_fibon[-1] + list_fibon[-2]
        list_fibon.append(temp)
        list_fibon.insert(0, -temp)
    print(list_fibon)



k = int(input("Введите количество элементов: "))

get_megafibon(k)