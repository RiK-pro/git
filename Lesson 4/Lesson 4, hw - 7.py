def fact(n):
    num = 1
    for el in range(1, n + 1):
        num = num * el
        yield f'{el}! = {num}'
n = int(input("Введите число для нахождения его факториала "))
for el in fact(n):
    print(el)