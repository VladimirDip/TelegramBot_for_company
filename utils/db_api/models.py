from sqlalchemy import sql, Column, BigInteger, Integer, String, DateTime, create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from .database import engine

engine = engine
Base = declarative_base()


class Catalogs(Base):
    __tablename__ = 'catalogs'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False)
    path = Column(String(250), nullable=False)
    download_date = Column(DateTime(), default=datetime.now)


class Admins(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    id_user = Column(BigInteger, nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    user_name = Column(String(150), nullable=False)
    date_comes_in_db = Column(DateTime(), default=datetime.now)


def table_exist(name):
    ret = inspect(engine).has_table(name)
    print('Table "{}" exists: {}'.format(name, ret))
    return ret


def create_db():
    match table_exist('catalogs') and table_exist('admins'):
        case True:
            print('база уже есть')
        case False:
            Base.metadata.create_all(engine)
            print('базы нет и была создана')



