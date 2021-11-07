#3
# -*- coding: utf-8 -*-
"""Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке."""

class Cell:
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __str__(self):
        return str(f"Клетка с количеством ячеек: {self.quantity}")

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        result = self.quantity - other.quantity
        if result < 0:
            return "Разность количества ячеек двух клеток меньше нуля"
        else:
            return result

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return round(self.quantity / other.quantity)

    @staticmethod
    def make_order(cell, quantity_in_row: int):
        items = '*' * cell.quantity
        finders = [items[idx:idx + quantity_in_row] for idx in range(0, len(items), quantity_in_row)]
        return '\n'.join(finders)

Cell_1 = Cell(12)
Cell_2 = Cell(15)

print("В расчётах участвуют клетки\n")
print(f"Cell1: {Cell_1}\n")
print(f"Cell2: {Cell_2}\n")
print(f"Результат сложения: {Cell_1 + Cell_2}")
print(f"Результат вычитания: {Cell_1 - Cell_2}")
print(f"Результат умножения: {Cell_2 * Cell_1}")
print(f"Результат деления: {Cell_2 / Cell_1}")
print("\nОрганизация по рядам первой клетки\n")
print(Cell.make_order(Cell_1, 5))
print("\nОрганизация по рядам второй клетки\n")
print(Cell.make_order(Cell_2, 5))