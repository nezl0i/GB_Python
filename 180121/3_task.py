# 3. Реализовать функцию  my_func() , которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    my_list = [arg1, arg2, arg3]
    my_list.remove(min(my_list))
    return my_list[0] + my_list[1]


print(my_func(2, 9, 7))
