from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'hw16'
DB_ECHO = True
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
    echo=False)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
