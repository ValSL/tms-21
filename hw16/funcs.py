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
    brand = relationship('Car', foreign_keys='Car.brand_id', backref='brand')

    def __repr__(self):
        return f'{self.id} {self.model} {self.release_year} {self.brand}'


def create_base():
    Base.metadata.create_all(engine)


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
    session.query(Brand).filter_by(Brand.id == choose).\
        delete(synchronize_session=False)


def update_brand():
    session = Session()
    print_available_brands()
    choose = int(input('Enter id: '))
    new_brand_name = input('Enter new brand name: ')
    session.query(Brand).filter_by(Brand.id == choose). \
        update({Brand.name: new_brand_name}, synchronize_session=False)



def enter_car():
    model = input('Enter model: ')
    release_year = int(input('Enter year: '))
    print('-----------------')
    print_available_brands()
    print('-----------------')
    brand_id = int(input('Enter brand id: '))
    return model, release_year, brand_id


def add_car():
    session = Session()
    model, year, brand_id = enter_car()
    brand = session.query(Brand).filter_by(Brand.id==brand_id)
    new_car = Car(
        model=model,
        release_year=year,
        brand=brand.name,
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
    session.query(Car).filter_by(Car.id == choose).\
        delete(synchronize_session=False)

