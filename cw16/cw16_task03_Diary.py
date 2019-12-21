from sqlalchemy import Column, Integer, ForeignKey
from cw16_base_engine import Base
from sqlalchemy.orm import relationship, backref


class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    avg_mark = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    student = relationship('Student',
                           foreign_keys='Diary.student_id',
                           backref=backref('diary', uselist=False))
