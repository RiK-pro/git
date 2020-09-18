def my_func1(x, y):
    print(f'Функция с "**" = {x ** y}')


def my_func2(x, y):
    n = 1
    i = 0
    while i < abs(y):
        n = (n * x)
        i += 1
    print(f'Функция с циклом = {1 / n}')


x = abs(float(input("Введите действительное положительное число Х - ")))
y = -abs(float(input("Введите целое отрицательное число Y - ")))
my_func1(x, y)
my_func2(x, y)
