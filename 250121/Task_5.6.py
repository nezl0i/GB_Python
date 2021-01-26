# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

dictionary = {}

with open("example_5.6.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        counter = 0
        for i, num in enumerate(line):
            if i == 0 or num == "—":
                continue
            else:
                num = int(num.split("(")[0])
                counter = counter + num
        dictionary[line[0][:-1]] = str(counter)

print(dictionary)
