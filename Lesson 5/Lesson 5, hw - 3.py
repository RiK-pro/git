with open("text_3.txt", "r", encoding="utf-8") as salary:
    s = []
    poor = []
    for i in salary:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        s.append(i[1])
print(f"Оклад меньше 20000 {poor}, средняя величина дохода сотрудников - {sum(map(float, s)) / len(s)}")
