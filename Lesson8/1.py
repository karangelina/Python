#1
"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
 (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных"""

class Data:
    def __init__(self, day_month_year: str):
        self.day_month_year = day_month_year

    @classmethod
    def extractor(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != "-": my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validator(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f"Дата записана верно"
                else:
                    return f"Год может быть только от 0 до 2021"
            else:
                return f"Месяц может быть только от 1 до 12"
        else:
            return f"День может быть только от 1 до 31"

print(Data.extractor("10 - 11 - 2021"))
print(Data.validator(11, 13, 2021))
print(Data.validator(10, 11, 2021))

