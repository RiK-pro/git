def func(x, y):
    try:
        result = x / y
    except ValueError:
        return print("Ввести можно только число")
    except ZeroDivisionError:
        return print("На ноль делить нельзя!")
    return result


x = int(input("Введите делимое "))
y = int(input("Введите делитель "))
print(func(x, y))
