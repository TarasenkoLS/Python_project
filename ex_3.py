class MyOneErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_func():
    my_list = []
    while True:
        num = input('Введите число или "q" (для выхода) ')
        if num.isdigit():
            my_list.append(num)
            print(f"{my_list}")
        elif num == 'q':
            return f"{my_list}"
        else:
            try:
                raise MyOneErr("Используем только цифры!")
            except MyOneErr as err:
                print(err)


print(my_func())

