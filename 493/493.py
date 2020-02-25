from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


# TODO: 创建user模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


# TODO: 创建Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey('user.id'))

    # TODO: 执行默认删除行为
    # authors = relationship('User', backref=backref('articles', cascade="save-update"), cascade="save-update")

    # TODO: 3.delete-orphan
    # TODO: 还需要在`子模型中的relationship中`，增加一个`single_parent=True的参数`。
    # authors = relationship('User', backref=backref('articles', cascade="save-update, delete, delete-orphan"),
    #                        cascade="save-update, delete", single_parent=True)

    # TODO: 4.merge：默认选项。
    # TODO: 当在使用session.merge，合并一个对象的时候，会将使用了relationship相关联的对象也进行merge操作。
    # authors = relationship('User', backref=backref('articles', cascade="save-update, delete, merge"),
    #                        cascade="save-update, delete, merge")

    # TODO: 6.all：是对save-update, merge, refresh-expire, expunge, delete几种的缩写
    authors = relationship('User', backref=backref('articles', cascade='all'), cascade='all')


# TODO: 初始化数据表
def init_db():
    # TODO：删除数据库
    Base.metadata.drop_all()
    # TODO: 创建数据库
    Base.metadata.create_all()

    # TODO: 添加数据
    user = User(name='zhiliao')
    article1 = Article(title='python')
    article2 = Article(title='flask')
    user.articles.append(article1)
    user.articles.append(article2)
    # TODO: 提交数据
    session.add(user)
    session.commit()


# TODO: 删除行为
def handle_delete():
    user = session.query(User).first()
    session.delete(user)
    session.commit()


# TODO: merge行为
def handle_merge():
    user = User(id=1, name='ketang')
    session.merge(user)
    session.commit()


if __name__ == '__main__':
    # init_db()   # TODO: 初始化数据表
    handle_delete()  # TODO: 删除行为
    # handle_merge()  # TODO: merge行为
