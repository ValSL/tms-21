from sqlalchemy.orm.session import sessionmaker
from database import Products, engine


def add_product(product: Products):
    session = sessionmaker(bind=engine)()
    session.add(product)
    session.commit()


def show_product(idd):
    session = sessionmaker(bind=engine)()
    q = session.query(Products).filter_by(id=idd).first()
    print(q)


def update_product(new_name: str, new_cost: int, new_count: int, new_comment: str, idd):
    session = sessionmaker(bind=engine)()
    q = session.query(Products).filter(Products.id == idd). \
        update({Products.name: new_name,
                Products.cost: new_cost,
                Products.count: new_count,
                Products.comment: new_comment}, synchronize_session=False)
    session.commit()