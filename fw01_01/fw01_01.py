from random import randint
import json
from datetime import datetime, date, time


def file_to_dict(filename: str):
    """Возвращает данные файла в типе списка"""
    with open(filename) as f:
        data = json.loads(f.read())
        file_dict = dict(data)
    return file_dict


def create_unique_id():
    file = file_to_dict('users.json')
    new_id = randint(1, 5)
    for value in file.values():
        if value['id'] == new_id:
            new_id = create_unique_id()
        else:
            continue
    return new_id


def create_new_user(name, second_name, profession, date_of_birth):
    with open('users.json') as f:
        data = json.loads(f.read())
        keys = data.keys()
        list_keys = list(keys)
    users = data
    new_user = {
        'name': name,
        'second_name': second_name,
        'profession': profession,
        'date_of_birth': date_of_birth,
        'id': create_unique_id()
    }
    users[len(list_keys)] = new_user

    with open('users.json', 'w') as f:
        data = json.dumps(users)
        f.write(data)


def delete_user(id):
    dict_file = file_to_dict('users.json')
    delete_key = 0
    id_list = []
    for keys, values in dict_file.items():
        id_list.append(keys)
        if values['id'] == id:
            delete_key = keys
    if delete_key not in id_list:
        print('net')
        return
    dict_file.pop(delete_key)
    with open('users.json', 'w') as f:
        data = json.dumps(dict_file)
        f.write(data)


def correction(id):
    dict_file = file_to_dict('users.json')
    for keys, values in dict_file.items():
        if values['id'] == id:
            print('''
                Что вы хотите изменить
                1) Имя
                2) Фамилия
                3) Дата рождения
                4) Профессия''')
            choose = input('Enter: ')
            if choose == '1':
                values['name'] = input('Введите новое имя: ')
            elif choose == '2':
                values['second_name'] = input('Введите новую фамилию: ')
            elif choose == '3':
                values['date_of_birth'] = input('Введите новую дату рождения: ')
            elif choose == '4':
                values['profession'] = input('Введите новую профессию: ')
            break
        dict_file[keys] = values

    else:
        print('Такого пользователя нет')

    with open('users.json', 'w') as f:
        data = json.dumps(dict_file)
        f.write(data)


def find():
    print('''
        По какому критерию искать
        1) Имя
        2) Фамилия
        3) Профессия
        4) Дата рождения
        5) ID''')
    choose = input('Enter: ')
    dict_file = file_to_dict('users.json')
    if choose == '1':
        enter = input('Введите имя: ')
        for keys, values in dict_file.items():
            if values['name'] == enter:
                print('Такой пользователь существует')
                print(dict_file[keys])
                break
        else:
            print('Такого пользователя не существует')
    if choose == '2':
        enter = input('Введите фамилию: ')
        for keys, values in dict_file.items():
            if values['second_name'] == enter:
                print('Такой пользователь существует')
                print(dict_file[keys])
                break
        else:
            print('Такого пользователя не существует')

    if choose == '3':
        enter = input('Введите профессию: ')
        for keys, values in dict_file.items():
            if values['profession'] == enter:
                print('Такой пользователь существует')
                print(dict_file[keys])
                break
        else:
            print('Такого пользователя не существует')

    if choose == '4':
        enter = input('Введите дату: ')
        for keys, values in dict_file.items():
            if values['date_of_birth'] == enter:
                print('Такой пользователь существует')
                print(dict_file[keys])
                break
        else:
            print('Такого пользователя не существует')

    if choose == '5':
        enter = int(input('Введите ID: '))
        for keys, values in dict_file.items():
            if values['id'] == enter:
                print('Такой пользователь существует')
                print(dict_file[keys])
                break
        else:
            print('Такого пользователя не существует')


def filter__print():
    print('''
        Выберите фильтрацию
        1) Пользователи дата рождения которых раньше заданной
        2) Пользователи дата рождения которых позже заданной''')
    choose = input('Enter: ')
    date_input = input('Введите дату: ')
    date_input = datetime.strptime(date_input, '%d.%m.%Y').date()
    dict_file = file_to_dict('users.json')
    if choose == '2':
        for keys, values in dict_file.items():
            if datetime.strptime(values['date_of_birth'], '%d.%m.%Y').date() > date_input:
                print(dict_file[keys])
    elif choose == '1':
        for keys, values in dict_file.items():
            if datetime.strptime(values['date_of_birth'], '%d.%m.%Y').date() < date_input:
                print(dict_file[keys])
    else:
        print('Таких нет')


def main():
    while True:
        print('''
            Выберите действие
        1) Создать пользователя
        2) Удалить пользователя
        3) Изменить пользователя
        4) Найти пользователя
        5) Фильтр
        0) Выход
        ''')
        choose = input('Enter: ')
        if choose == '0':
            break
        if choose == '1':
            file = file_to_dict('users.json')
            if len(file) == 5:
                print('Лимит')
                continue
            name = input('Введите имя: ')
            sec_name = input('Введите фамилию: ')
            prof = input('Введитн профессию: ')
            birth_date = input('Введите дату рождения в формате D.M.Y: ')
            create_new_user(name, sec_name, prof, birth_date)
            input('press enter')
        if choose == '2':
            i = int(input('id: '))
            delete_user(i)
            input('press enter')
        if choose == '3':
            i = int(input('id: '))
            correction(i)
            input('press enter')
        if choose == '4':
            find()
            input('press enter')
        if choose == '5':
            filter__print()
            input('press enter')


if __name__ == '__main__':
    main()
