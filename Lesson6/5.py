#5
"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""

class Stationery:
    title: str

    def draw(self):
        return "Запуск отрисовки."

class Pen(Stationery):
    title = "Отрисовка ручкой"

    def draw(self):
        return self.title

class Pencil(Stationery):
    title = "Отрисовка карандашом"

    def draw(self):
        return self.title

class Handle(Stationery):
    title = "Отрисовка маркером"

    def draw(self):
        return self.title


p = Pen()
pn = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(h.draw())
print(p.draw())
print(pn.draw())




