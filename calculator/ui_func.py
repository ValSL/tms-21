import func
from exceptions import NumOnlyException

def ui():
    while True:
        print('''Выберите действие: 
                1) Сложение
                2) Вычитание
                3) Умножение 
                4) Деление
                0) Выход''')
        enter = input('Enter: ')
        try:
            if enter.isdigit() == False:
                raise NumOnlyException
        except NumOnlyException:
            print('Введите число')
            continue
        if enter == '1':
            print('Введите два числа: ')
            try:
                number_1 = int(input('Число 1: '))
                number_2 = int(input('Число 2: '))
            except ValueError:
                print('Введены неверные числа!')
                input('press enter')
                continue
            print(func.add(number_1, number_2))
        elif enter == '2':
            print('Введите два числа: ')
            try:
                number_1 = int(input('Число 1: '))
                number_2 = int(input('Число 2: '))
            except ValueError:
                print('Введены неверные числа!')
                input('press enter')
                continue
            print(func.diff(number_1, number_2))
        elif enter == '3':
            print('Введите два числа: ')
            try:
                number_1 = int(input('Число 1: '))
                number_2 = int(input('Число 2: '))
            except ValueError:
                print('Введены неверные числа!')
                input('press enter')
                continue
            print(func.mul(number_1, number_2))
        elif enter == '4':
            print('Введите два числа: ')
            try:
                number_1 = int(input('Число 1: '))
                number_2 = int(input('Число 2: '))
            except ValueError:
                print('Введены неверные числа!')
                input('press enter')
                continue
            try:
                res = func.div(number_1, number_2)
            except ZeroDivisionError:
                print('Деление на 0!!!')
                input('press enter')
                continue
            print(res)
        elif enter == '0':
            break
        else:
            print('Такого варианта нет!')
            input('press enter')
