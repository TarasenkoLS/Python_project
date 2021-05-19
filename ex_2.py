class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def weight_as(self, thickness):
        rez = self._length * self._width * 25 * thickness / 1000
        print(f"Для покрытия автодороги длинной {self._length} м., шириной {self._width} м. и"
              f" толщиной полотна {thickness} см. потребуется {rez} тонн асфальта")


road_1 = Road(20, 5000)
road_1.weight_as(5)
