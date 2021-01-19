# 6. Реализовать функцию  int_func() , принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например,  print(int_func(‘text’)) -> Text.


def int_func(user_text):
    return user_text.title()


default_text = input('Введите текст: ')
print(int_func(default_text))
