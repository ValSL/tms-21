from sqlalchemy import Column, Integer, String, ForeignKey, Table
from cw16_base_engine import Base
from sqlalchemy.orm import relationship, backref
from cw16_classes import Student #тут это нужно, для таблицы ассоциаций, чтобы она видела student.id


association_table = Table('assotiations', Base.metadata,
                          Column('student_id', Integer, ForeignKey('student.id')),
                          Column('book_id', Integer, ForeignKey('book.id')))


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    book_name = Column(String)
    pages = Column(Integer)
    student = relationship('Student',
                           secondary=association_table,
                           backref='books')




