# 6
"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""

# 6.1
def int_func(a):
        return a.title()
print(int_func("text"))

# 6.2
def my_func(a):
    separate_words = a.split(" ")
    total = []
    for el in separate_words:
        string_element = str(el)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func("hello world"))