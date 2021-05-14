def fact(n):
    f = 1
    for i in range(n + 1):
        f = f * (i + 1)
        yield f'{i}! = {f}'


for el in fact(10):
    print(el)
