season_list = ["winter", "spring", "summer", "autumn"]
season_dict = {1: "winter", 2: "spring", 3: "summer", 4: "autumn"}
month = int(input("Введите месяц в виде целого числа от 1 до 12 "))
if month == 12 or month == 1 or month == 2:
    print("list - " + season_list[0])
    print("dict - " + season_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print("list - " + season_list[1])
    print("dict - " + season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print("list - " + season_list[2])
    print("dict - " + season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print("list - " + season_list[3])
    print("dict - " + season_dict.get(4))
else:
    print("Такого месяца не существует")
