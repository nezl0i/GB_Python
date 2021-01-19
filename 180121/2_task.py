# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def person(name, surname, age, street, email, phone):
    return ' '.join([name, surname, age, street, email, phone])


print(person(name='Max', surname='Pupkin', age='1979', street='Moskow', phone='+7927123456', email='pupkin@mail.ru'))
