from sqlalchemy.orm import relationship, sessionmaker
from cw16 import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, MetaData, ForeignKey

Base = declarative_base()


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'id = {self.id}, name = {self.name}'


class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(
        Integer, ForeignKey('artist.id'), nullable=False)

    artist = relationship(
        'Artist', foreign_keys='Album.artist_id', backref='albums')


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    group_id = Column(
        Integer, ForeignKey('group.id'), nullable=False)
    group = relationship(
        'Group', foreign_keys='Student.group_id', backref='students')


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
