# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

print('Enter text to write file "text.txt"')

with open("example_5.1.txt", 'w') as f:
    user_str = True
    while user_str:
        user_str = input()
        f.write(user_str + '\n')
