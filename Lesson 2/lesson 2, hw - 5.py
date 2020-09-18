my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
new = int(input("Введите число "))
for el in range (len(my_list)):
    if new == my_list[el]:
        my_list.insert(el, new)
        break
    elif new > my_list[0]:
        my_list.insert(0, new)
    elif new < my_list[-1]:
        my_list.append(new)
    elif new < my_list[el] and new > my_list[el + 1]:
        my_list.insert(el + 1, new)
        break
print(my_list)
