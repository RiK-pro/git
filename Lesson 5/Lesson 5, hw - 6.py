my_dict = {}
with open("text_6.txt", "r", encoding="utf-8") as lessons:
    for line in lessons:
        name, numb = line.split(":")
        name_sum = sum(map(int, "".join([i for i in numb if i == " " or (i >= "0" and i <= "9")]).split()))
        my_dict[name] = name_sum
print(my_dict)
