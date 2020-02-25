from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime
import time

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


# TODO: 定义User模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    create_time = Column(DATETIME, nullable=False, default=datetime.now)

    def __repr__(self):
        return '<User(id={id}, name={name}, create_time={create_time})>'.format(id=self.id, name=self.name,
                                                                                create_time=self.create_time)


# TODO: 定义Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, nullable=False, default=datetime.now)

    uid = Column(Integer, ForeignKey('user.id'))

    # TODO: 在模型中定义relationship的order_by参数: 正序
    # authors = relationship('User', backref=backref('articles', order_by=create_time))

    # TODO: 在模型中定义relationship的order_by参数: 倒序
    # authors = relationship('User', backref=backref('articles', order_by=create_time.desc()))

    authors = relationship('User', backref=backref('articles'))

    # TODO: 3.在模型中定义__mapper_args__: 正序
    # __mapper_args__ = {
    #     'order_by': create_time
    # }

    # TODO: 3.在模型中定义__mapper_args__: 倒序
    __mapper_args__ = {
        'order_by': create_time.desc()
    }

    def __repr__(self):
        return '<Article(id=%s, title=%s, create_time=%s)>' % (self.id, self.title, self.create_time)


# TODO: 删除数据表
# Base.metadata.drop_all()
# TODO: 创建数据表
# Base.metadata.create_all()

# TODO: 新增数据
# user = User(name='zhiliao')
# article1 = Article(title='python')
# user.articles.append(article1)
# session.add(user)
# session.commit()
#
# time.sleep(2)
#
# article2 = Article(title='flask')
# user.articles.append(article2)
# session.add(user)
# session.commit()
#
# time.sleep(2)
#
# article3 = Article(title='django')
# user.articles.append(article3)
# session.add(user)
# session.commit()

# TODO: 1.order_by
# TODO: 1.1 正序排序
# articles = session.query(Article).order_by(Article.create_time).all()
# articles = session.query(Article).order_by('create_time').all()
# print(articles)

# TODO: 1.2 倒序排序
# articles = session.query(Article).order_by(Article.create_time.desc()).all()
# articles = session.query(Article).order_by('-create_time').all()
# print(articles)

# TODO: 2.在模型中定义relationship的order_by参数
# TODO: 2.1 正序排序
# TODO: 2.2 倒序排序
# TODO: 3.在模型中定义__mapper_args__
# TODO: 3.1 正序排序
# TODO: 3.2 倒序排序
users = session.query(User).first()
print(users.articles)
