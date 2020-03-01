from sqlalchemy import create_engine, Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/alembic_demo?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)


# TODO: 定义User模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    # TODO: 6.以后如果修改了模型，重复4、5步骤
    age = Column(Integer, nullable=False)
    create_time = Column(DATETIME, default=datetime.now)


# TODO: 定义Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey('user.id'))

    authors = relationship('User', backref=backref('articles'))

    # TODO: 6.以后如果修改了模型，重复4、5步骤
    create_time = Column(DATETIME, default=datetime.now)

# TODO: 读取当前文件父目录(绝对路径)
# import os
# import sys
# print(sys.path)
# print(os.path.dirname(__file__))    # TODO: D:/github/python-flask/501

# TODO: 读取当前文件父目录的父目录(绝对路径)
# print(os.path.dirname(os.path.dirname(__file__)))   # TODO: D:/github/python-flask
