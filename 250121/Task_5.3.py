# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих
# сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

salary = 20000
count = 0
total = 0
work_list = []

with open("example_5.3.txt") as f:
    for line in f:
        surname, wages = line.strip().split()
        total += float(wages)
        if float(wages) < salary:
            work_list.append(surname)
        count += 1
    total_wages = total / count
print(f'{work_list} \nСредний доход всех сотрудников: {total_wages:.02f}')
