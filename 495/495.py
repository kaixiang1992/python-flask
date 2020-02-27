from sqlalchemy import create_engine, Column, Integer, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


# TODO: 定义Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)

    def __repr__(self):
        return '<Article(id={id}, title={title}, create_time={create_time})>'.format(id=self.id,
                                                                                     title=self.title,
                                                                                     create_time=self.create_time)


# TODO: 删除数据表
# Base.metadata.drop_all()
# TODO: 新建数据表
# Base.metadata.create_all()

# TODO: 创建数据
# for x in range(100):
#     article = Article(title='title %s' % x)
#     session.add(article)
# session.commit()

# TODO: 1.limit：可以限制每次查询的时候只查询几条数据。
# TODO: 正序查询10条数据
# articles = session.query(Article).order_by(Article.id).limit(10).all()
# TODO: 倒序查询10条数据
# articles = session.query(Article).order_by(Article.id.desc()).limit(10).all()
# print(articles)

# TODO: 2.offset：可以限制查找数据的时候过滤掉前面多少条。
# TODO: 查询第id: 10-19条数据
# articles = session.query(Article).offset(9).limit(10).all()
# print(articles)

# TODO: 3.切片slice(start,stop)方法来做切片操作
# TODO: 正序查询前10条
# articles = session.query(Article).order_by(Article.id).slice(0, 10).all()
# TODO: 倒序查询前10条
# articles = session.query(Article).order_by(Article.id.desc()).slice(0, 10).all()
# print(articles)

# TODO: 4.切片使用`[start:stop]`的方式来进行切片操作
# TODO: 正序查询前10条
# articles = session.query(Article).order_by(Article.id)[0:10]
# TODO: 倒序查询前10条
articles = session.query(Article).order_by(Article.id.desc())[0:10]
print(articles)
