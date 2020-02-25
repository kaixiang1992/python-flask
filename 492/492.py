from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

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


# TODO: 定义Article文章模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey('user.id'))

    # TODO: 1. cascade=""不会提交任何数据
    # authors = relationship('User', backref=backref('articles', cascade=""))

    # TODO: 2.cascade="save-update"把其他和他相关联的数据都添加到数据库中
    # authors = relationship('User', backref=backref('articles', cascade="save-update"))

    # TODO: 3.cascade="delete"当删除某一个模型中的数据的时候，是否也`删掉使用relationship和他关联的数据`
    authors = relationship('User', backref=backref('articles', cascade='save-update,delete'))


# TODO: 创建comment模型
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    context = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey('user.id'))

    authors = relationship('User', backref=backref('comments'))


# TODO: 初始化数据表数据
def init_db():
    # TODO: 删除所有数据表
    Base.metadata.drop_all()
    # TODO: 创建数据表
    Base.metadata.create_all()

    # TODO: 创建数据
    user = User(name='zhiliao')
    article1 = Article(title='python基础语法')
    article2 = Article(title='flask基础语法')
    comment1 = Comment(context='python大法好...')
    comment2 = Comment(context='人生苦短，我用python...')
    user.articles.append(article1)
    user.articles.append(article2)
    user.comments.append(comment1)
    user.comments.append(comment2)

    # TODO: 提交数据
    session.add(user)
    session.commit()


# TODO: 执行删除操作
def handle_delete():
    # TODO: 通过user删除关联article
    user = session.query(User).first()

    # TODO: 通过article删除数据不会关联删除user
    # article = session.query(Article).first()
    # TODO: 提交数据
    session.delete(user)
    session.commit()


if __name__ == '__main__':
    # init_db()
    handle_delete()
