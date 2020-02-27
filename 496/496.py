from sqlalchemy import create_engine, Column, Integer, String, DATETIME, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


# TODO: 定义User用户模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)

    def __repr__(self):
        return '<User(name=%s)>' % self.name


# TODO: 定义Article文章模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)

    authors = relationship('User', backref=backref('articles', lazy="dynamic"), uselist=False)

    def __repr__(self):
        return '<Article(title=%s, uid=%s)>' % (self.title, self.uid)


# TODO: 删除数据表
# Base.metadata.drop_all()
# TODO: 创建数据表
# Base.metadata.create_all()


# TODO: 创建数据
# user = User(name='zhiliao')
# for x in range(100):
#     article = Article(title='title %s' % x)
#     article.authors = user
#     session.add(article)
# TODO: 提交数据
# session.commit()

from sqlalchemy.orm.query import Query
# TODO: <class 'sqlalchemy.orm.query.Query'>
# TODO: 查询数据
# user = session.query(User)
# print(type(user))   # TODO: <class 'sqlalchemy.orm.query.Query'>

from sqlalchemy.orm.dynamic import AppenderQuery

# TODO: 查询数据
# TODO: <class 'sqlalchemy.orm.dynamic.AppenderQuery'>
# user = session.query(User).first()
# print(user.articles)
# print(type(user.articles))

# TODO: <class 'sqlalchemy.orm.query.Query'>
# TODO: 查询数据
# user = session.query(User).first()
# articles = user.articles.filter(Article.id > 80)
# print(articles)
# print(type(articles))   # TODO: <class 'sqlalchemy.orm.query.Query'>

# TODO: 查询数据
user = session.query(User).first()
articles = user.articles.filter(Article.id > 80).all()
print(articles)
