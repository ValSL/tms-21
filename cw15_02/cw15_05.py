from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, and_
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///test.db", echo=True)
metadata = MetaData()
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.add(Person('Alex', 'Varkalov'))
session.add_all([Person('Alex', 'Petrov'), Person('Ann', 'Ivanova')])
session.commit()

person = session.query(Person)
print('-----------------------')
print(person)
person = session.query(Person).filter_by(firstname="Alex").first()
print('-----------------------')
print(person.firstname)

person = session.query(Person).filter(
   Person.firstname=="Alex").first()

person = session.query(Person).filter(and_(
  Person.firstname=="Alex",
  Person.lastname=="Varkalov",
)).all()
