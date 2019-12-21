from sqlalchemy.orm import sessionmaker
from cw16_base_engine import engine
from cw16_task04_Book import Book
from cw16_classes import Student

session = sessionmaker(bind=engine)()

students = session.query(Student).all()
student_list = []
for student in students:
    student_list.append(student)

book1 = Book(book_name='book1', pages=100, student=student_list)
book2 = Book(book_name='book2', pages=200, student=student_list)
book3 = Book(book_name='book3', pages=300, student=student_list)
book4 = Book(book_name='book4', pages=400, student=student_list)
book5 = Book(book_name='book5', pages=500, student=student_list)
books = [book1, book2, book3, book4, book5]
session.add_all(books)

session.commit()
