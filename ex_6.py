def int_func():
    w = input("Введите слово латинскими буквами в нижнем регистре ")
    for i in set(w):
        if 96 < ord(i) < 123:
            w.title()
        else:
            print("Условие ввода не выполнено!")
    return w.title()


print(int_func())
