# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input()

count = int(input('Укажите количество элементов в списке: '))
user_list = []
for i in range(count):
    items = int(input(f'Введите {i+1}-й элемент списка: '))
    user_list.append(items)
print(user_list)

for k in range(1, len(user_list), 2):
    user_list[k - 1], user_list[k] = user_list[k], user_list[k - 1]
print(user_list)
