i = 0
with open("text_1.txt", "r", encoding="utf=8") as moon:
    print(f"Содержимое файла:\n{moon.read()}")
    moon.seek(0)
    for line in moon:
        i += 1
        line.strip()
        spl = line.split()

        print(f"Строка №{i} - длина строки {len(spl)} слов: {line}")
print(f"Количество строк в файле: {i}")