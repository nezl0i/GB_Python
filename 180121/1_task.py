# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.

int_a = input('Введите число А: ')
int_b = input('Введите число В: ')


def func_devision(val_a, val_b):
    try:
        return int(val_a) / int(val_b)
    except ZeroDivisionError:
        print('Деление на 0 запрещено!')
    except ValueError:
        print('Одно из значений не является числом')


print(func_devision(int_a, int_b))
