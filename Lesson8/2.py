# 2
"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой"""

class Division(Exception):
    def __init__(self, txt):
        self.txt = txt

def division_func():
    try:
        dividend = int(input("Введите делимое:"))
        divider = int(input("Введите делитель:"))
        if divider == 0:
            raise Division("Делить на 0 нельзя!")
        else:
            result = dividend / divider
            return result
    except ValueError:
        return "Вы ввели не число"
    except Division as error:
        return error

print(division_func())