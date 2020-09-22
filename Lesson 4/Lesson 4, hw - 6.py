from itertools import count, cycle
"""Первое задание"""
try:
    i = count(int(input("Введите целое число для генератора ")))
    for n in range(10):
        print(next(i), end=' ')
except ValueError:
    print("Значение должно быть целым числом")

"""Второе задание"""
my_list = ["Do it", 2, 4.392]
c = 0
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1