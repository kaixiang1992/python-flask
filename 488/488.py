from sqlalchemy import create_engine, Column, Integer, String, DATETIME, TEXT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
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

    # articles = relationship('Article')

    def __repr__(self):
        return '<User(id={id}, username={username})>'.format(id=self.id, username=self.username)


# TODO: 定义文章表模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(TEXT, nullable=False)
    context = Column(TEXT, nullable=False)

    uid = Column(Integer, ForeignKey('user.id', ondelete="RESTRICT"))
    user = relationship('User', backref="articles")

    def __repr__(self):
        return '<Article(title={title}, uid={uid})>'.format(title=self.title, uid=self.uid)


# TODO: 1.未使用`relationship`进行相关联的表查询 -- 一对一
# TODO: 根据文章发布人ID查询发布人信息
article = session.query(Article).first()
# print(article)
user = session.query(User).filter(User.id == article.uid).first()
# print(user)

# TODO: 2.使用`relationship`进行表管理查询 -- 一对一
# TODO: 根据文章关联发布人查询发布人信息
article1 = session.query(Article).first()
# print(article1)
# print(article1.user)

# TODO: 3.使用`relationship`进行表管理查询  -- 一对多
# TODO: 根据发布人信息查询发布所有文章信息
user_articles = session.query(User).first()
# print(user_articles)
# print(user_articles.articles)

# TODO: 3.使用`relationship`参数`backref`进行表管理查询  -- 一对多
# TODO: 根据发布人信息查询发布所有文章信息
user_articles1 = session.query(User).first()
print(user_articles1)
print(user_articles1.articles)

