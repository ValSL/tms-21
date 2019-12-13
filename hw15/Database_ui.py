import functions
from database import Products, engine
from sqlalchemy.orm.session import sessionmaker

while True:
    print(''''Выберите действие:
1) Добавление в базу
2) Просмотр по id
3) Изменение по id''')
    inp = input('Enter: ')
    if inp == '0':
        break
    elif inp == '1':
        name = input('Введите название: ')
        cost = int(input('Введите цену: '))
        count = int(input('Введите количество: '))
        comment = input('Введите комментарий: ')
        functions.add_product(Products(name, cost, count, comment))
        input('press enter')
    elif inp == '2':
        id = int(input('Введите id: '))
        functions.show_product(id)
        input('press enter')
    elif inp == '3':
        inp_id = int(input('Введите id: '))

        lst = []
        session = sessionmaker(bind=engine)()
        s = session.execute('select id from products')
        for id in s:
            lst.append(id[0])
        if inp_id not in lst:
            print('Такого id нет')
            input('press enter')
            continue

        name = input('Введите название: ')
        cost = int(input('Введите цену: '))
        count = int(input('Введите количество: '))
        comment = input('Введите комментарий: ')
        functions.update_product(name, cost, count, comment, inp_id)
