# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

# Вариант 1
with open("example_5.2.txt") as f:
    content = f.readlines()
    print(f'Количество строк в файле - {len(content)}')
    count = 1
    for el in content:
        print(f'Строка {count} - слов {len(el.split(" "))}')
        count += 1

# Вариант 2
# try:
#     with open("example.txt", 'r') as f:
#         count = 0
#         for line in f:
#             print(f'Строка {count + 1} - слов {len(line.split(" "))}')
#             count += 1
#         print(f'Количество строк в файле - {count}')
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
