# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
from random import randint

def min_count_coin(coin):
    reverse_coin = 0
    tails_coin = randint(1, coin-1)
    print(f'Монет лежащих решкой: {tails_coin}')
    eagle_coin = coin - tails_coin
    print(f'Монет лежащих орлом: {eagle_coin}')
    if tails_coin > eagle_coin:
        reverse_coin = eagle_coin
    else:
        reverse_coin = tails_coin
    return reverse_coin

        

try:
    count_coin = int(input('Введите количество монет: '))
    print(f'Количество монет которые нужно перевернуть: {min_count_coin(count_coin)}')
except:
    print('Введено некорректное значение')