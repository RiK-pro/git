def func (what):
    my_list = []
    for el in what:
        summ = int(el)
        my_list.append(summ)
    return sum(my_list)
x = 0
while True:
    try:
        inp = input("Введите строку чисел и нажмите ENTER, или любой символ для выхода ").split()
        n = func(inp)
        x = n + x
        print(f"{n} ({x})")
    except ValueError:
        print("Выход из программы")
        print(f"Итог: {n} ({x})")
        break
