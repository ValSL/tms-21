from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from cw17_db import Base


association_table = Table('book_student_association', Base.metadata,
   Column('student_id', Integer, ForeignKey('student.id')),
   Column('book_id', Integer, ForeignKey('book.id'))
)


class Book(Base):
   __tablename__ = 'book'
   id = Column(Integer, primary_key=True)
   title = Column(String)
   pages = Column(Integer)
   students = relationship('Student', secondary=association_table, backref='books')
