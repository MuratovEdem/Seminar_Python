# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

import random

def compose_polynomial(k: int) -> str:
    number_list = [random.randint(-10, 10) for _ in range(k + 1)]
    polynomial = ""
    for i, coefficient in enumerate(number_list):
        if coefficient == 0:
            continue
        degree = k - i
        if degree == 0:
            if coefficient > 0:
                polynomial += f" + {coefficient}"
            else:
                polynomial += f" - {abs(coefficient)}"
        elif degree == 1:
            if coefficient > 0:
                if coefficient == 1:
                    polynomial += f" + x"
                else:
                    polynomial += f" + {coefficient}x"
            else:
                if coefficient == -1:
                    polynomial += f" - x"
                else:
                    polynomial += f" - {abs(coefficient)}x"
        else:
            if coefficient > 0:
                if coefficient == 1:
                    polynomial += f" + x^{degree}"
                else:
                    polynomial += f" + {coefficient}x^{degree}"
            else:
                if coefficient == -1:
                    polynomial += f" - x^{degree}"
                else:
                    polynomial += f" - {abs(coefficient)}x^{degree}"
    if polynomial.startswith(" + "):
        polynomial = polynomial[3:]
    else:
        polynomial = polynomial.lstrip()
    return polynomial + " = 0"


# Пример использования функции
k = int(input('Введите максимальное значение степени многочлена: '))

print(compose_polynomial(k))
