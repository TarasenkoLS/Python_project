def int_func(w):
    """
    Принимает слова из маленьких латинских букв и возвращает их же но с с прописной первой буквой
    :param w: str
    :return: str
    """
    for i in set(w):
        if 96 < ord(i) < 123:
            w.title()
        else:
            return print("Ошибка! Функция принимает только латинские буквы в нижнем регистре!")
    return w.title()


s = input("Введите слова через пробел (используйте латинские буквы в нижнем регистре)\n").split()
rez = []
for word in s:
    rez.append(int_func(word))
print(' '.join(rez))
