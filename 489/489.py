from sqlalchemy import create_engine, Column, Integer, String, DATETIME, TEXT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.orm.collections import InstrumentedList
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


# TODO: 定义用户表模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(11), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)

    # TODO: 一对多模式，uselist=True，允许列表添加多个
    # extend = relationship('User_Extend', uselist=True)

    # TODO: 一对一模式，uselist=Faslse，允许对象而非列表
    # extend = relationship('User_Extend', uselist=False)

    def __repr__(self):
        return '<User(id={id}, username={username})>'.format(id=self.id, username=self.username)


# TODO: 定义用户额外信息模型
class User_Extend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

    # TODO: 外键管理`user`表`id`字段
    uid = Column(Integer, ForeignKey('user.id'))

    # TODO: 一对多模式，uselist=True，允许列表添加多个
    # TODO: 一对一模式，uselist=Faslse，允许对象而非列表
    # user = relationship('User')

    # TODO: 借助`sqlalchemy.orm.backref`来简化代码
    user = relationship('User', backref=backref('extend', uselist=False))

    def __repr__(self):
        return '<User_Extend(uid={uid}, country={country}, city={city})>'.format(self.uid, country=self.country,
                                                                                 city=self.city)


# TODO: 定义文章表模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(TEXT, nullable=False)
    context = Column(TEXT, nullable=False)
    uid = Column(Integer, ForeignKey('user.id', ondelete="RESTRICT"))
    create_time = Column(DATETIME, default=datetime.now)

    user = relationship('User', backref="articles")

    def __repr__(self):
        return '<Article(title={title}, uid={uid})>'.format(title=self.title, uid=self.uid)


# TODO: 删除数据库
Base.metadata.drop_all()
# TODO: 创建数据库
Base.metadata.create_all()

# TODO: 一对多添加数据，user添加至article
# user = User(username='zhiliao')
# article1 = Article(title='title1', context='abc abc')
# article2 = Article(title='title2', context='abc abc')
# print(user.articles)  # TODO: list
# print(type(user.articles))  # TODO: <class 'sqlalchemy.orm.collections.InstrumentedList'>  => 本质是一个list列表
# user.articles.append(article1)
# user.articles.append(article2)

# TODO: 一对多模式，uselist=True，允许列表添加多个
# user = User(username='zhiliao')
# user_extend1 = User_Extend(country='中国', city='长沙')
# user_extend2 = User_Extend(country='中国', city='杭州')
# user.extend.append(user_extend1)
# user.extend.append(user_extend2)

# TODO: 一对一模式，uselist=Faslse，允许对象而非列表
# TODO: 借助`sqlalchemy.orm.backref`来简化代码
user = User(username='zhiliao')
user_extend = User_Extend(country='中国', city='杭州')
print(user.extend)  # TODO: None
print(type(user.extend))  # TODO: <class 'NoneType'>
user.extend = user_extend

# TODO: 提交数据
session.add(user)
session.commit()
