rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("new_text_4.txt", "a", encoding="utf-8") as new:
    with open("text_4.txt", encoding="utf-8") as file:
        line = file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new.writelines(rus[i[0]] + " - " + i[1] + "\n")
