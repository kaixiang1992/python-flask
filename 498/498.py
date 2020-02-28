from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DATETIME, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime

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
    create_time = Column(DATETIME, default=datetime.now)


# TODO: 定义Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)
    # TODO: 外键约束
    uid = Column(Integer, ForeignKey('user.id'))

    authors = relationship('User', backref=backref('articles', uselist=True), uselist=False)


# TODO: 删除数据表后创建数据表
# Base.metadata.drop_all()
# Base.metadata.create_all()

# TODO: 添加测试数据
# user1 = User(name='zhiliao')
# user2 = User(name='ketang')

# TODO: user1 一篇文章
# for x in range(1):
#     article = Article(title='title %s' % x)
#     article.authors = user1
#     session.add(article)
# session.commit()

# TODO: user2 两篇文章
# for x in range(1, 3):
#     article = Article(title='title %s' % x)
#     article.authors = user2
#     session.add(article)
# session.commit()


# TODO: 1.join进行内连接查询user.name及文章数量，根据文章数量进行倒序排序
# sql: TODO:  select user.name,count(article.id) as article_count from user join article on user.id=article.uid group by user.id order by article_count desc;
result = session.query(User.name, func.count(Article.id)).join(Article, User.id == Article.uid).group_by(User.id).order_by(func.count(Article.id).desc()).all()
print(result)   # TODO: [('ketang', 2), ('zhiliao', 1)]
