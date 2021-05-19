class Stationery:
    def __init__(self, title="Название канцелярской принадлежности"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(F"Начинаем рисовать ручкой {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(F"Начинаем рисовать карандашом {self.title}")


class Handle(Stationery):
    def draw(self):
        print(F"Начинаем рисовать маркером {self.title}")


s1 = Pen("Закорючка")
s1.draw()
s2 = Pencil("Конструктор")
s2.draw()
s3 = Handle("Чертежник")
s3.draw()
