import json

with open("text_7.txt", encoding="utf-8") as my_f:
    dict_1 = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in my_f}
    prof = [val for val in dict_1.values() if val > 0]
    list_all = [dict_1, {"av_pr": sum(prof) / len(prof)}]
    print(list_all)

with open("text_7j.json", "w", encoding="utf-8") as my_j:
    json.dump(list_all, my_j, ensure_ascii=False, indent=4)
