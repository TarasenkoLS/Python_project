from random import randint

with open("text_5.txt", 'w+', encoding="utf-8") as f5:
    list_f5 = [randint(1, 100) for i in range(5, 50)]
    f5.write(" ".join(map(str, list_f5)))
    f5.seek(0)
    print(sum(map(int, f5.readline().split())))
