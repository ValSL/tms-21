from sqlalchemy.orm.session import sessionmaker
from database import Products, engine

session = sessionmaker(bind=engine)()


def add_product():
    name = input('Введите название: ')
    cost = int(input('Введите цену: '))
    count = int(input('Введите количество: '))
    comment = input('Введите комментарий: ')
    product = Products(name, cost, count, comment)
    session.add(product)
    session.commit()


def show_product():
    inp_id = int(input('Введите id: '))
    q = session.query(Products).filter_by(id=inp_id).first()
    print(q)


def update_product():
    inp_id = int(input('Введите id: '))

    lst = []
    s = session.execute('select id from products')
    for id in s:
        lst.append(id[0])
    if inp_id not in lst:
        print('Такого id нет')
        input('press enter')
        return

    name = input('Введите название: ')
    cost = int(input('Введите цену: '))
    count = int(input('Введите количество: '))
    comment = input('Введите комментарий: ')
    q = session.query(Products).filter(Products.id == inp_id). \
        update({Products.name: name,
                Products.cost: cost,
                Products.count: count,
                Products.comment: comment}, synchronize_session=False)
    session.commit()


def delete_product():
    inp_id = int(input('Введите id: '))
    q = session.query(Products).filter(Products.id == inp_id).\
        delete(synchronize_session=False)
    session.commit()
