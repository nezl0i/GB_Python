# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

russin_list = ['Один', 'Два', 'Три', 'Четыре']
count = 0
write_list = []

# Вариант 1
# with open("example_5.4.2.txt", 'w') as file:
#     with open('example_5.4.txt') as f:
#         for line in f:
#             en_word, number = line.split(" - ")
#             file.write(f'{russin_list[count]} - {number}')
#             count += 1

# Вариант 2
with open('example_5.4.txt') as f:
    for line in f:
        en_word, number = line.split(" - ")
        write_list.append(f'{russin_list[count]} - {number}')
        count += 1

with open('example_5.4.2.txt', 'w') as f:
    f.writelines(write_list)
