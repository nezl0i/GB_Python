# 7. Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно
# сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию  int_func() .

def int_func(user_text):
    return user_text.title()


def capitalize_string(line):
    return ' '.join(s[:1].upper() + s[1:] for s in line.split(' '))


default_text = input('Введите текст: ')

print(int_func(default_text))
print(capitalize_string(default_text))
