from sqlalchemy.orm import sessionmaker
from cw16_base_engine import engine
from cw16_classes import Student
from cw16_task03_Diary import Diary
from random import randint

session = sessionmaker(bind=engine)()

students = session.query(Student).all()

for student in students:
    session.add(Diary(avg_mark=randint(1, 10), student=student))

session.commit()
