def client_info(**kwargs):
    print(f'{client_info.get(var_2)} {client_info.get(var_1)}, год рождения: {client_info.get(var_3)}, город проживания: {client_info.get(var_4)}, email: {client_info.get(var35)}, номер телефона: {client_info.get(var6)}')


client_info(
    var_1=input("Введите имя: "),
    var_2=input("Введите фамилию: "),
    var_3=input("Введите год рождения: "),
    var_4=input("Введите город проживания: "),
    var_5=input("Введите ваш email: "),
    var_6=input("Введите ваш номер телефона: "))
print(client_info.get(var_2))