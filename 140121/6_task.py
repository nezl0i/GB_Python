# 6. *Реализовать структуру данных  «
# Товары »  . Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента  — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.

default_dict = {}
result = []
new_list = []
result_analitic = {}
default_key = ["Название", "Цена", "Количество", "ед."]
count = range(4)
b = int(input('Укажите количество товаров: '))
b += 1
full_count = range(1, b)

for m in full_count:
    new_dict = (m,)
    for i in count:
        dict_str = input(f'Введите {default_key[i]} товара {m} ')
        default_dict[default_key[i]] = dict_str
    new_dict += (default_dict.copy(),)
    result.append(new_dict)
print(result)

for el_list in result:
    new_list.append(tuple(el_list[1].values()))

result_array = zip(*new_list)
total_list = list(result_array)

for k in count:
    result_analitic[default_key[k]] = list(total_list[k])
print(result_analitic)
