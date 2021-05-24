class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        print("Сложение ячеек 2х клеток")
        return self.number + other.number

    def __sub__(self, other):
        print("Вычитаем количество ячеек 2й клетки из количества ячеек 1й клетки")
        if self.number > other.number:
            return self.number - other.number
        else:
            return "Операция не может быть выполеннена, разность должна быть больше нуля"

    def __mul__(self, other):
        print("Умножение ячеек 2х клеток")
        return self.number * other.number

    def __truediv__(self, other):
        print("Делим количество ячеек 1й клетки на количества ячеек 2й клетки")
        if other.number > 0:
            return round(self.number / other.number, 2)
        else:
            return "Операция не может быть выполенена, делить на 0 нельзя!"

    def make_oder(self, s):
        return "\n".join(["*" * s for i in range(self.number // s)]) + "\n" + "*" * (self.number % s)


cell_1 = Cell(25)
cell_2 = Cell(50)
print(f" {cell_1.number}, {cell_2.number}")
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_oder(4))

