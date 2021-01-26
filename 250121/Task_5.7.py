# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json

firm_json = []
profit = {}
average_profit = 0
i = 0
with open('example_5.7.txt') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit[name] >= 0:
            average_profit = average_profit + profit[name]
            i += 1
    firm_json.append(profit)
    firm_json.append({'average_profit': average_profit / i})
    print(f'Json object {firm_json}')

with open('file_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(firm_json, write_js, ensure_ascii=False)
