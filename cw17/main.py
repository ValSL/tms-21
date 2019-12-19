from sqlalchemy.orm import sessionmaker
from group import Group
from student import Student
from book import Book
from cw17_db import engine
from cw17_db import Base

Base.metadata.create_all(engine)


def main():
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all([])
    session.commit()


if __name__ == '__main__':
    main()
