my_f = open("text_1.txt", "w", encoding="utf-8")
line = " "
while line:
    line = input("Введите содержимое строки, или пустая строка для выхода\n")
    my_f.write(f"{line}\n") if line != "" else my_f.close()
