def dict_sum_num(list_x):
    x = list_x.split(":")
    list_i = x[1].split()
    s = 0
    for el in list_i:
        num = '0'
        for i in el:
            if i.isdigit():
                num += i
        s += int(num)
    return {x[0]: s}


m = 'Informatics: 40(л) 12(пр) 20(лаб)'
print(dict_sum_num(m))

with open("text_6.txt", encoding="utf-8") as my_f:
    my_dict = {}
    for line in my_f:
        my_dict.update(dict_sum_num(line))
    print(my_dict)