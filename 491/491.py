from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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

    def __repr__(self):
        return '<User(id={id}, name={name})>'.format(id=self.id, name=self.name)


# TODO: 创建Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    # TODO: 外键约束
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)

    authors = relationship('User', backref='articles')


# TODO: 删除数据库
# Base.metadata.drop_all()
# TODO: 创建数据库
# Base.metadata.create_all()
#
# user = User(name='zhiliao')
# article1 = Article(title='python')
# article2 = Article(title='flask')
#
# user.articles.append(article1)
# user.articles.append(article2)

# TODO: 提交数据
# session.add(user)
# session.commit()

# TODO: 1.session.delete进行删除，不指定`nullable=False`
# TODO: 2.session.delete进行删除，指定`nullable=False`，避免删除行为
user = session.query(User).first()
print(user)
session.delete(user)
session.commit()
