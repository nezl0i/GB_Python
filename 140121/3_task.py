# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

season = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
month = int(input('Введите номер месяца (1-12): '))

if month > 12:
    print('Неверное значение.')
else:
    for key, value in season.items():
        if month in value:
            print(key)
