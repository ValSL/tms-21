from cw16_base_engine import engine
from cw16_task03_Diary import Diary
from cw16_classes import Album, Artist, Group, Student
from cw16_base_engine import Base
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

group1 = Group(name='Group_1')
group2 = Group(name='Group_2')
artist = Artist(name='MyBand')
album = Album(name='MyAlbum', artist=artist)
student1 = Student(name='Student_one', group=group1)
student2 = Student(name='Student_two', group=group1)
student3 = Student(name='Student_three', group=group1)
student4 = Student(name='Student_four', group=group2)
student5 = Student(name='Student_five', group=group2)
student6 = Student(name='Student_six', group=group2)
session.add_all([artist, album, group1, group2, student1, student2, student3, student4, student5, student6])
session.commit()
