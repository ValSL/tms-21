from hw16_db_connect import engine
from sqlalchemy import Column, Integer, String, ForeignKey
from hw16_db_connect import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

Session = sessionmaker(bind=engine)


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'{self.id} {self.name}'


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    brand = relationship('Brand', foreign_keys='Car.brand_id')

    def __repr__(self):
        return f'{self.id} {self.model} {self.release_year} {self.brand}'


def create_base():
    Base.metadata.create_all(engine)


def get_brand(brand_id):
    session = Session()
    brand = session.query(Brand).filter_by(id=brand_id).first()
    session.close()
    return brand


def print_available_brands():
    session = Session()
    brands = session.query(Brand).all()
    print('Available brands id')
    for brand in brands:
        print(brand)


def enter_brand():
    brand = input('Enter brand: ')
    return brand


def add_brand():
    session = Session()
    brand_name = enter_brand()
    new_brand = Brand(
        name=brand_name
    )
    session.add(new_brand)
    session.commit()


def delete_brand():
    session = Session()
    print_available_brands()
    choose = int(input('Enter id: '))
    session.query(Brand).filter(Brand.id == choose).\
        delete(synchronize_session=False)
    session.commit()


def update_brand():
    session = Session()
    print_available_brands()
    choose = int(input('Enter id: '))
    new_brand_name = input('Enter new brand name: ')
    session.query(Brand).filter(Brand.id == choose). \
        update({Brand.name: new_brand_name}, synchronize_session=False)
    session.commit()


def enter_car():
    model = input('Enter model: ')
    release_year = int(input('Enter year: '))
    print('-----------------')
    print_available_brands()
    print('-----------------')
    brand_id = int(input('Enter brand id: '))
    brand = get_brand(brand_id)
    return model, release_year, brand


def add_car():
    session = Session()
    model, year, brand = enter_car()
    new_car = Car(
        model=model,
        release_year=year,
        brand=brand,
    )
    session.add(new_car)
    session.commit()


def delete_car():
    session = Session()
    cars = session.query(Car).all()
    print('Available brands id')
    for car in cars:
        print(car.id)
    choose = int(input('Enter id: '))
    session.query(Car).filter(Car.id == choose).\
        delete(synchronize_session=False)


def print_cars():
    session = Session()
    cars = session.query(Car).all()
    for car in cars:
        print(f'{car.id}|{car.model}|{car.release_year}|{car.brand.name}')


def choose_car_param():
    print('\nChoose the parameter which you want to update:',
          '1. Model',
          '2. Brand',
          '3. Release year')
    param_dict = {
        1: 'model',
        2: 'brand',
        3: 'release_year',
    }
    param_num = int(input('Enter param num: '))
    return param_dict[param_num]


def update_car():
    car_id = int(input('Enter car id: '))
    paramater = choose_car_param()
    session = Session()
    if paramater == 'brand':
        print_available_brands()
        brand_id = int(input("Enter brand id: "))
        session.query(Car).filter(Car.id == car_id). \
            update({Car.brand_id: brand_id})
        session.commit()
        return
    new_value = input('Enter new value: ')
    session.query(Car).filter(Car.id==car_id). \
        update({paramater: new_value})
    session.commit()

