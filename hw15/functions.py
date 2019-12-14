from sqlalchemy.orm.session import sessionmaker
from database import Products, engine
from MyExceptions import OnlyString

session = sessionmaker(bind=engine)()
id_lst = []
s = session.execute('select id from products')
for id in s:
    id_lst.append(id[0])


def validate_input():
    name, cost, count, comment = (None, None, None, None)
    while True:
        try:
            name = input('Введите название: ')
            if name.isdigit():
                raise OnlyString()
            cost = int(input('Введите цену: '))
            count = int(input('Введите количество: '))
            comment = input('Введите комментарий: ')
            if comment.isdigit():
                raise OnlyString()
            break
        except ValueError:
            print('Введите число!')
            continue
        except OnlyString:
            print('Введите текст')
            continue
    return name, cost, count, comment


def add_product():
    name, cost, count, comment = validate_input()
    product = Products(name, cost, count, comment)
    session.add(product)
    session.commit()


def show_product():
    inp_id = int(input('Введите id: '))
    if inp_id not in id_lst:
        print('Такого id нет')
        return
    q = session.query(Products).filter_by(id=inp_id).first()
    print(q)


def update_product():
    inp_id = int(input('Введите id: '))

    if inp_id not in id_lst:
        print('Такого id нет')
        return
    name, cost, count, comment = validate_input()

    session.query(Products).filter(Products.id == inp_id). \
        update({Products.name: name,
                Products.cost: cost,
                Products.count: count,
                Products.comment: comment}, synchronize_session=False)
    session.commit()


def delete_product():
    inp_id = int(input('Введите id: '))
    if inp_id not in id_lst:
        print('Такого id нет')
        return
    session.query(Products).filter(Products.id == inp_id). \
        delete(synchronize_session=False)
    session.commit()
