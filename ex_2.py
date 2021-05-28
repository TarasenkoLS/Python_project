class MyOneErr(Exception):
    def __init__(self, txt):
        self.txt = txt


d_1 = input("Введите делимое ")
d_2 = input("Введите делитель ")

try:
    d_1 = int(d_1)
    d_2 = int(d_2)
    if d_2 == 0:
        raise MyOneErr("Деление на ноль запрещено!")
except ValueError:
    print("Вы ввели не число")
except MyOneErr as err:
    print(err)
else:
    print(f"{d_1} / {d_2} = {round(d_1 / d_2, 2)}")