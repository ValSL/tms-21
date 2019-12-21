from sqlalchemy.orm import relationship
from cw16_base_engine import Base
from sqlalchemy import Column, String, Integer, ForeignKey


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

    def __repr__(self):
        return f'id-{self.id}, name-{self.name}'
