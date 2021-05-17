my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "five": "Пять",
           "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}


with open('text_4ru.txt', 'w', encoding="utf-8") as f_ru:
    with open('text_4.txt', encoding="utf-8") as f:
        f_ru.writelines([line.replace(line.split()[0], my_dict.get(line.split()[0])) for line in f])
