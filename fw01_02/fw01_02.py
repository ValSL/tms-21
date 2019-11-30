import csv
from datetime import datetime, date, time
from random import randint


def csv_read(csv_filename='users.csv'):
    rows = []
    with open(csv_filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        fields = next(csvreader)
        for line in csvreader:
            rows.append(line)
    return fields, rows


def csv_write(lines: list, name='users.csv'):
    fields = ['name', 'sec_name', 'prof', 'birth_date', 'id']
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(lines)


def csv_user_create(lines: list):
    fields, rows = csv_read()
    rows += lines
    csv_write(rows)


def csv_user_delete(id):
    fields, rows = csv_read()
    for index, line in enumerate(rows):
        if line[4] == id:
            rows.pop(index)
            csv_write(rows)
            return
    else:
        print('Такого пользователя нет')


def csv_user_change(id):
    fields, rows = csv_read()
    for index, lines in enumerate(rows):
        if lines[4] == id:
            print('''Что вы хотите изменить
                    1) Имя
                    2) Фамилия
                    3) Профессия
                    4) Дата рождения''')
            choose = input('Enter: ')
            if choose == '1':
                new_name = input('Введите новое имя:')
                lines[0] = new_name
            elif choose == '2':
                new_sec_name = input('Введите новую фамилию:')
                lines[1] = new_sec_name
            elif choose == '3':
                new_prof = input('Введите новую профессию:')
                lines[2] = new_prof
            elif choose == '4':
                new_date = input('Введите новую дату рождения:')
                lines[3] = new_date
            csv_write(rows)
            break
    else:
        print('Такого пользователя нет')


def csv_print(id):
    fields, rows = csv_read()
    for col in fields:
        print(col.ljust(30, " "), end='')
    print()
    for row in rows:
        if row[4] == id:
            for col in row:
                print(col.ljust(30, " "), end='')
            print()


def csv_user_find():
    fields, rows = csv_read()
    print('''
        Выберите по какомц критерию искать
        1) Имя
        2) Фамилия
        3) Профессия 
        4) Дата рождения
        5) ID''')
    choose = input('Enter: ')
    if choose == '1':
        inp = input('Введите имя: ')
        for index, line in enumerate(rows):
            if line[0] == inp:
                print('Такой пользователь есть')
                csv_print(line[4])
            if index == (len(rows) - 1):
                break
            continue
        else:
            print('Такого пользователя нет')

    elif choose == '2':
        inp = input('Введите фамилию: ')
        for index, line in enumerate(rows):
            if line[1] == inp:
                print('Такой пользователь есть')
                csv_print(line[4])
            if index == (len(rows) - 1):
                break
            continue
        else:
            print('Такого пользователя нет')

    elif choose == '3':
        inp = input('Введите профессию: ')
        for index, line in enumerate(rows):
            if line[2] == inp:
                print('Такой пользователь есть')
                csv_print(line[4])
            if index == (len(rows) - 1):
                break
            continue
        else:
            print('Такого пользователя нет')

    elif choose == '4':
        inp = input('Введите дату: ')
        for index, line in enumerate(rows):
            if line[3] == inp:
                print('Такой пользователь есть')
                csv_print(line[4])
            if index == (len(rows) - 1):
                break
            continue
        else:
            print('Такого пользователя нет')

    elif choose == '5':
        inp = input('Введите ID: ')
        for index, line in enumerate(rows):
            if line[4] == inp:
                print('Такой пользователь есть')
                csv_print(line[4])
            if index == (len(rows) - 1):
                break
            continue
        else:
            print('Такого пользователя нет')


def csv_filter():
    pass


def main():
    while True:
        print('''
            Выберите действие
        1) Создать пользователя
        2) Удалить пользователя
        3) Изменить пользователя
        4) Найти пользователя
        5) Фильтр
        ''')
        choose = input('Enter: ')
        if choose == '0':
            break
        if choose == '1':
            name = input('Введите имя: ')
            sec_name = input('Введите фамилию: ')
            prof = input('Введите профессию: ')
            birth_date = input('Введите дату рождения в формате Day.Month.Year: ')
            lines = [name, sec_name, prof, birth_date, randint(100, 500)]
            csv_user_create([lines])
            input('press enter')
        if choose == '2':
            i = input('id: ')
            csv_user_delete(i)
            input('press enter')
        if choose == '3':
            i = input('id: ')
            csv_user_change(i)
            input('press enter')
        if choose == '4':
            csv_user_find()
            input('press enter')
        # if choose == '5':
        #     filter()
        #     input('press enter')
        #
if __name__ == '__main__':
    main()
