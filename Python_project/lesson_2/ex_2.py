my_list = [i for i in input('Введите значения списка через пробел ').split()]
print(my_list)
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)
