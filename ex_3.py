with open('text_3.txt', encoding="utf-8") as f:
    count = 0
    sum_ = 0
    for line in f:
        count += 1
        sum += float(line.split()[1])
        if float(line.split()[1]) < 20000.0:
            print(line.split()[0])
print(f"Средний доход на струдника - {sum_ / count}")
