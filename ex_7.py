class ComplexData:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}j"

    def __add__(self, other):
        print(f"Сумма {ComplexData.__str__(self)} и {ComplexData.__str__(other)}")
        return f"{self.a + other.a}+{self.b + other.b}j"

    def __mul__(self, other):
        print(f"Произведение {ComplexData.__str__(self)} и {ComplexData.__str__(other)}")
        return f"{self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}j"


n_1 = ComplexData(7, 5)
n_2 = ComplexData(8, 10)
print(n_1 + n_2)
print(n_1 * n_2)
