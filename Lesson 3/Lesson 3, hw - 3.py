def my_func(a, b, c):
    if a >= b and c >= b:
        return a + c
    if a >= c and b >= c:
        return a + b
    if b >= a and c >= a:
        return b + c


a = (int(input("Введите первое число ")))
b = (int(input("Введите второе число ")))
c = (int(input("Введите третье число ")))
print(f"Результат - {my_func(a, b, c)}")
