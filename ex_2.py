from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @property
    @abstractmethod
    def consump(self):
        pass

    def __add__(self, other):
        return round(self.consump + other.consump, 2)


class Suit(Clothes):

    @property
    def consump(self):
        if 1.60 < self.param < 2.30:
            return round(2 * self.param + 0.3, 2)
        else:
            print("Изготавливаем костюмы на рост от 1.60м. до 2.30м.")
            return 0


class Coat(Clothes):
    @property
    def consump(self):
        if 38 <= self.param <= 58:
            return round((self.param / 6.5 + 0.5), 2)
        else:
            print("Изготавливаем польто размеры от 38 до 58")
            return 0

    def __add__(self, other):
        self.coat_cons = self.consump + other.consump
        return self.coat_cons


suit_1 = Suit("Сударь", 1.7)
print(suit_1.consump)
coat_1 = Coat("Apple", 44)
print(coat_1.consump)
print(suit_1 + coat_1)
