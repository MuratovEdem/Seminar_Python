# Даны два многочлена, которые вводит пользователь. как две строки.
# Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.

# Степени многочленов могут быть разные.

# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re

import copy


def result_calc_polynomial(polynomial_input_1: str, polynomial_input_2: str) -> str:
    dict_polynomial_1 = creating_dictionary(polynomial_input_1)
    dict_polynomial_2 = creating_dictionary(polynomial_input_2)
    calc_element = calc_elements_dict(dict_polynomial_1, dict_polynomial_2)
    return compose_result_polyn(calc_element)


def creating_dictionary(polynom: str) -> dict:
    temp_list = split_string_in_list(polynom)
    dict_result = {}
    for i in temp_list:
        if 'x' not in i:
            dict_result[0] = int(i)
        else:
            value, key = [word.strip() for word in i.split("x")]
            key = key.replace("^", "")
            if key == "":
                key = '1'
                if value == '-' or value == '+':
                    dict_result[int(key)] = int(value + '1')
                else:
                    dict_result[int(key)] = int(value)
            elif int(key) > 1:
                if value == '-' or value == '+':
                    dict_result[int(key)] = int(value + '1')
                else:
                    dict_result[int(key)] = int(value)
    return dict_result


def split_string_in_list(polyn: str) -> list:
    polyn = polyn.replace(" = 0", "")
    polyn = polyn.replace("+ ", "+")
    polyn = polyn.replace("- ", "-")
    polyn = polyn.replace("*", "")
    list_result = polyn.split()
    return list_result


def calc_elements_dict(dict_polyn_1: dict, dict_polyn_2: dict) -> dict:
    temp_dict = copy.deepcopy(dict_polyn_1)
    for key, value in dict_polyn_2.items():
        if temp_dict.get(key, False):
            temp_dict[key] = value + temp_dict[key]
        else:
            temp_dict[key] = value
    sorted_dict = dict(sorted(temp_dict.items(), key=lambda x: x[0], reverse=True))
    return sorted_dict


def compose_result_polyn(dict_res: dict) -> str:
    polynomial = ""
    for key, value in dict_res.items():
        if key == 0:
            if value > 0:
                polynomial += f" + {value}"
            else:
                polynomial += f" - {abs(value)}"
        elif key == 1:
            if value > 0:
                if value == 1:
                    polynomial += f" + x"
                else:
                    polynomial += f" + {value}x"
            else:
                if value == -1:
                    polynomial += f" - x"
                else:
                    polynomial += f" - {abs(value)}x"
        else:
            if value > 0:
                if value == 1:
                    polynomial += f" + x^{key}"
                else:
                    polynomial += f" + {value}x^{key}"
            else:
                if value == -1:
                    polynomial += f" - x^{key}"
                else:
                    polynomial += f" - {abs(value)}x^{key}"
    if polynomial.startswith(" + "):
        polynomial = polynomial[3:]
    else:
        polynomial = polynomial.lstrip()
    return polynomial + " = 0"





# polynomial_1 = int(input('Введите перый многочлен: '))

# polynomial_2 = int(input('Введите второй многочлен: '))

polynomial_1 = '-5 + 4x + 2x^2 - 7x^5 = 0'

polynomial_2 = '11x^2 - 5x^8 + 4 - 5x^3 - 3*x^4 - 12 = 0'

result_polyn = result_calc_polynomial(polynomial_1, polynomial_2)

print(result_polyn)

