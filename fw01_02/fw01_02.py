import csv
from datetime import datetime, date, time
from random import randint


def csv_write(lines: list, name='users.csv'):
    fields = ['name', 'sec_name', 'prof', 'birth_date', 'id']
    with open(name, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(lines)

def csv_read(csv_filename: str):
    rows = []
    with open(csv_filename, 'r') as my_file:
        csvreader = csv.reader(my_file)
        fields = next(csvreader)
        for line in csvreader:
            rows.append(line)
    return fields, rows


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
            csv_write([lines])
            input('press enter')
        # if choose == '2':
        #     i = int(input('id: '))
        #     delete_user(i)
        #     input('press enter')
        # if choose == '3':
        #     i = int(input('id: '))
        #     correction(i)
        #     input('press enter')
        # if choose == '4':
        #     find()
        #     input('press enter')
        # if choose == '5':
        #     filter()
        #     input('press enter')
        #
if __name__ == '__main__':
    main()
