my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list_new = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(my_list_new)

my_l = [128, 18, 21, 26, 12, 45, 0, 15, 87, 36, 21, 45]
m_l = [my_l[el] for el in range(1, len(my_l)) if my_l[el] > my_l[el - 1]]
print(m_l)
