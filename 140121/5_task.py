# 5. Реализовать структуру  «  Рейтинг »  , представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.

default_list = [8, 6, 5, 4, 3, 3, 1]

key = int(input('Введите элемент рейтинга: '))

try:
    index = default_list.index(key)
    count = default_list.count(key)
    default_list.insert(index + count, key)
    # print(index, '-', count)
    print(default_list)
except ValueError:
    print('Элемент в списке не найден.')
    for element in default_list[::-1]:
        if element > key:
            index = default_list.index(element)
            default_list.insert(index + 1, key)
            print(default_list)
            break
        else:
            default_list.insert(0, key)
            print(default_list)
            break
