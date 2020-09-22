from sys import argv

"""Для формулы использовал данные: 160 часов, 350 оплата в час и 25000 премия"""
try:
    name, prod, rate, bonus = argv
    salary = (int(prod) * int(rate) + int(bonus))
    print(f"Программа для вычисления заработной платы")
    print(f"Сотрудник отработал: {prod} часов в месяц")
    print(f"Ставка сотрудника: {rate} рублей в час")
    print(f"Премия сотрудника: {bonus} рублей")
    print(f"Месячная зарплата сотрудника составит {salary} рублей")
except ValueError:
    print("Не хватает параметров, или параметр введен неверно")