def my_func(n_1, n_2, n_3):
    """принимает 3 позиционных аргумента и возвращает сумму 2х наибольших"""
    list_num = sorted([n_1, n_2, n_3])
    return sum(list_num[1:])


print(my_func(-15, 36, 15))
