from sqlalchemy import create_engine, Column, Integer, String, DATETIME, ForeignKey, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


# TODO: 定义文章表模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(TEXT, nullable=False)
    context = Column(TEXT, nullable=False)

    # TODO: 1.RESTRICT：父表数据被删除，会阻止删除。默认就是这一项。
    # uid = Column(Integer, ForeignKey('user.id', ondelete="RESTRICT"))

    # TODO: 2.NO ACTION：在MySQL中，同RESTRICT。
    # uid = Column(Integer, ForeignKey('user.id', ondelete='NO ACTION'))

    # TODO: 3.CASCADE：级联删除。
    # uid = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))

    # TODO: 4.SET NULL：父表数据被删除，子表数据会设置为NULL。
    uid = Column(Integer, ForeignKey('user.id', ondelete='SET NULL'))


Base.metadata.drop_all()
Base.metadata.create_all()

# TODO: 添加用户表数据
user1 = User(username='zhiliao')
user2 = User(username='ketang')

session.add_all([user1, user2])
# TODO: 提交数据
session.commit()

# TODO: 添加文章表数据
article1 = Article(title='title1', context='abc abc', uid=1)
article2 = Article(title='title2', context='abc abc', uid=1)
article3 = Article(title='title3', context='def def', uid=2)
article4 = Article(title='title4', context='def def', uid=2)

session.add_all([article1, article2, article3, article4])
# TODO: 提交数据
session.commit()
