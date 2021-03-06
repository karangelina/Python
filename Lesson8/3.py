#3
# -*- coding: utf-8 -*-
"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только
числами. Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться"""

class NotNumber(Exception):
    def __init__(self, number):
        self.number = number

result_list = []

while True:
    value = input("Введите значение для добавления в список или введите stop, чтобы выйти:")
    if value == "stop":
        print(f"Текущий список: {result_list}")
        break
    try:
        if not value.isnumeric():
            raise NotNumber(f"Введено не число")
        result_list.append(int(value))
    except NotNumber as error:
        print(f"Введено не число")