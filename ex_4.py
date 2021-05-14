print("Определяем эелементы списка, не имеющие повторений")

list_1 = [10, 12, 2, 7, 5, 2, 15, 7, 11, 45, 7, 12, 2, 7]
list_2 = [el for el in list_1 if list_1.count(el) == 1]

print(f"Вариант 1:\nИсходный список: {list_1}\nРезультат: {list_2}\n")


from random import randint

list_a = [randint(-5, 15) for i in range(3, 20)]
list_b = [el for el in list_a if list_a.count(el) == 1]
print(f"Вариант 2:\nИсходный список: {list_a}\nРезультат: {list_b}\n")