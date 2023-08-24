# Напишите программу, которая принимает на вход целое или дробное число и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

from decimal import Decimal

def number_counter(number):
    if number == 0:
        return 1
    number_1 = int(number)
    number_2 = number-number_1
    count = 0
    if number_1 == 0:
        count = 1

    while number_1 > 0:
      count += 1
      number_1=number_1//10
      
    while number_2 != int(number_2):
        count += 1
        number_2*=10
  
    return count



try:
    number = Decimal(input("Введите число: "))
    print (f'В данном числе - {number_counter(number)} цифр')
except:
    print ("Введено некорректное значение")


