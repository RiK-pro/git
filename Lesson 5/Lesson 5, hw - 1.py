try:
    with open("text_1.txt", "w", encoding="utf=8") as moon:
        while True:
            user_text = input("Введите строку для записи в файл. Для остановки программы оставьте поле пустым и нажмите Enter\n")
            if user_text == "":
                break
            else:
                print(user_text, file=moon)

except IOError:
    print("Ошибка")

with open("text_1.txt", "r", encoding="utf=8") as moon:
    my_f = moon.readlines()
    print(my_f)