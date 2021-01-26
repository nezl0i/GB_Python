# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

list_number = "11 2 45 32 14 5 15 24 77 41 11 8"
total = 0

with open("example_5.5.txt", 'w+') as f:
    f.writelines(list_number)
    f.seek(0)
    for line in f:
        for num in line.split():
            total += int(num)
        print(line.split())
        print(f'Сумма чисел: {total}')
