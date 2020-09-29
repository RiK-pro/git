def summary():
    try:
        with open('calc.txt', 'w+') as calculator:
            line = input('Введите цифры через пробел \n')
            calculator.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Нужно ввести только цифры')
summary()