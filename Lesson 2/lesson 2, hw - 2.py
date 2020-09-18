count = int(input("Сколько значений будет в списке? "))
my_list = []
n = 0
el = 0
while n < count:
    my_list.append(input("Введите следующее значение списка "))
    n += 1

for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
