a = int(input("Сколько км пробегает спортсмен за день? "))
b = int(input("А какая финальная цель в км? "))
day = 1
while a < b:
    a = a * 1.1
    day += 1
print(f"Спортсмен достигнет цель на {day} день")