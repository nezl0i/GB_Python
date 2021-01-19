# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.


total = 0

while True:
    int_array = input('Enter values: ').split()
    if '*' in int_array:
        int_array = list(map(lambda x: int(x), int_array[:int_array.index('*')]))
        total += sum(int_array)
        print(total)
        break
    try:
        int_array = list(map(lambda x: int(x), int_array))
        total += sum(int_array)
        print(total)
    except ValueError:
        print('Enter incorrect value')
