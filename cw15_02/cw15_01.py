from sqlalchemy import create_engine

e = create_engine("sqlite:///test.db")
e.execute("""
   create table user (
       id integer primary key autoincrement,
       firstname varchar,
       lastname varchar
   )
""")