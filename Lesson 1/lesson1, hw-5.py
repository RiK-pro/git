income = int(input("Введите доход вашей фирмы за прошлый год "))
costs = int(input("А какие были расходы? "))
if income > costs:
    profit = (income - costs)
    print(f"Ваша фирма является прибыльной, рентабельность вашей выручки {income/profit*100:.0f}%")
    workers = int(input("А сколько работников у вас в фирме? "))
    print(f"Фирма заработала {profit/workers:.2f} в расчёте на одного сотрудника")
elif income == costs:
    print("Фирма работает в ноль, сожалеем")
elif income < costs:
    print("Ваша фирма убыточная, задумайтесь")
