a = abs(int(input("Введите целое положительное число ")))
b = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > b:
        b = a % 10
    if a > 9:
        continue
    else:
        print("Самая большая цифра в этом числе ", b)
    break