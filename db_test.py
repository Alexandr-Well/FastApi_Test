from sqlalchemy import create_engine, inspect
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy.engine import Inspector
from sqlalchemy.testing import db
from sqlalchemy_utils import database_exists
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = "postgresql+psycopg2://postgres:root@localhost:5432/test"

base = declarative_base()


class User(base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return f"<User(name= {self.name}, id= {self.id})>"


if not database_exists(DB_NAME):
    connection = psycopg2.connect(user="postgres", password="root")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    # Создаем базу данных
    cursor.execute('create database test')
    # Закрываем соединение
    cursor.close()
    connection.close()

engine = create_engine(DB_NAME, echo=True, pool_size=6,
                       max_overflow=10)
engine.connect()

if not inspect(engine).has_table("test"):
    print(inspect(engine).has_table("test"), "as")
    base.metadata.create_all(engine)
print(inspect(engine).has_table("test"))


from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

session = sessionmaker(bind=engine)()

if session.query(User).filter_by(name='a2').first() is None:
    user_1 = User(name="a2")

    session.add(user_1)
    session.commit()
    print("!!!!!!!!!!!!!!!")
    print(user_1)
users = session.query(User).filter_by(name='a2')
ses = session.execute("SELECT * FROM test")
print(ses.all())
# print(session.query(User).all())


