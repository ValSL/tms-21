from hw16_db_connect import engine
from sqlalchemy import Column, Integer, String, ForeignKey
from hw16_db_connect import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

session = sessionmaker(bind=engine)()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand = Column(String, ForeignKey('brand.name'), nullable=False)


def create_base():
    Base.metadata.create_all(engine)


def print_available_brands():
    brands = session.query(Brand).all()
    print('Available brands id')
    for brand in brands:
        print(f'id:{brand.id} - name:{brand.name}')


def enter_brand():
    brand = input('Enter brand: ')
    return brand


def enter_car():
    model = input('Enter model: ')
    release_year = int(input('Enter year: '))
    print_available_brands()
    brand_id = int(input('Enter brand id: '))
    return model, release_year, brand_id


def add_brand():
    brand_name = enter_brand()
    new_brand = Brand(
        name=brand_name
    )
    session.add(new_brand)
    session.commit()


def add_car():
    model, year, brand_id = enter_car()
    brand = session.query(Brand).filter_by(Brand.id==brand_id)
    new_car = Car(
        model=model,
        release_year=year,
        brand=brand.name,
    )
    session.add(new_car)
    session.commit()


def delete_brand():
    print_available_brands()
    choose = int(input('Enter id: '))
    session.query(Brand).filter_by(Brand.id == choose).\
        delete(synchronize_session=False)


def delete_car():
    cars = session.query(Car).all()
    print('Available brands id')
    for car in cars:
        print(car.id)
    choose = int(input('Enter id: '))
    session.query(Car).filter_by(Car.id == choose).\
        delete(synchronize_session=False)

