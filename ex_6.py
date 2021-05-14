from itertools import count, cycle
import random
import string
# a
iter_a = count(5)
for i in range(10):
    print(next(iter_a))
# b
# Создаем список из случайных букв
list_1 = list(random.choice(string.ascii_uppercase) for i in range(4))
iter_b = cycle(list_1)
n = 3 # количество повторений всех элементов списка
for i in range(len(list_1)*n):
    print(next(iter_b))

