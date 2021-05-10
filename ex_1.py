def my_f(arg_1, arg_2):
    """"""
    try:
        return arg_1 / arg_2
    except ZeroDivisionError:
        print("Ошибка! Деление на 0!")


try:
    rezult = my_f(float(input("Введите делимое: ")), float(input("Введите делитель: ")))

    if rezult is not None:
        print(rezult)
except ValueError:
    print("Ошибка! Для ввода данных необходимо использовать только цифры 0-9.")
