my_list = [54, 37, 24, 15, 8]
n = float(input("Введите натуральное число (целое число >0): "))
if n > 0:
    my_list.append(n)
    my_list.sort(reverse=True)
else:
    print("Введенное число не является натуральным!")
print(my_list)
