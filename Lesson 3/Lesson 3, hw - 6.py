def func(a):
    return a.title()


print(func("text"))


def my_func():
    for word in input("Введите набор слов из маленьких латинских букв через пробел: ").split():
        letters = 0
        for el in word:
            if ord(el) >= 97 and ord(el) <= 122:
                letters += 1
        if letters == len(word):
            print(word.title())
        else:
            print(f"{word} - требуются только маленькие символы латиницей")


my_func()
