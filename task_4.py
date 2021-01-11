# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


user_number = int(input('Введите число: '))

max_number = 0
while user_number > 10:
    i = user_number % 10
    user_number //= 10
    if i > max_number:
        max_number = i
print(max_number)


