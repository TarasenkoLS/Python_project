my_f = open("text_1.txt", "r", encoding="utf-8")
ind = 1
for ind, line in enumerate(my_f, 1):
    print(f"В {ind}-й строке слов - {len(line.split())}, символов - {len(line) - 1}.")
print(f"В файле {my_f.name} всего {ind} строк")
my_f.close()
