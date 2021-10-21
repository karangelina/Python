# 2
"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""

def my_function(name, surname, birth_year, city, email, phone):
    print(f"{name} {surname} {birth_year} {city} {email} {phone}")

my_function(name = "Angelina", surname = "Karnaukhova", birth_year = 1996, city = "Irkutsk", email = "email@icloud.com", phone = "89999999999")