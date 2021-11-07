#2
# -*- coding: utf-8 -*-
"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def textile(self):
        pass

class Coat(Clothes):
    def __init__(self, name, v):
        self.v = v
        super().__init__(name)

    @property
    def textile(self):
        return round(self.v / 6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, name, h):
        self.h = h
        super().__init__(name)

    @property
    def textile(self):
        return round(2 * self.h + 0.3, 2)

Coat_1 = Coat("Lichi", 20)
print(f"Для пошива пальто {Coat_1.name} нужно {Coat_1.textile}")

Suit_1 = Suit("Lichi", 6)
print(f"Для пошива костюма {Suit_1.name} нужно {round(2 * Suit_1.h + 0.3, 2)}")

def sum_textile(clothes: list[Clothes]):
    list = []
    for n in clothes:
        list.append(n.textile)
    return sum(list)

print(f"\nОбщий расход ткани равен {sum_textile([Coat_1, Suit_1])}")