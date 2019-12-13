from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('sqlite:///hw15.db')
Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)
    count = Column(Integer)
    comment = Column(String)

    def __init__(self, name, cost, count, comment):
        self.name = name
        self.cost = cost
        self.count = count
        self.comment = comment

    def __repr__(self):
        return f'name = {self.name}, cost = {self.cost}, count = {self.count}, comment = {self.comment}'


Base.metadata.create_all(engine)





