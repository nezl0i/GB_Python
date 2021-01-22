# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
import math


def my_factorial():
    n = 0
    while True:
        n += 1
        yield n


fact_obj = my_factorial()

try:
    user_value = int(input('Enter value: '))
    for el in fact_obj:
        if el <= user_value:
            print(f'{el}! = {math.factorial(el)}')
        else:
            break
except ValueError:
    print('This no number entered')



