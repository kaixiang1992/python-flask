from sqlalchemy import create_engine, Column, Integer, String, DATETIME, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

# TODO: 创建数据库引擎
engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()

# TODO: 2.使用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”。
article_tag = Table(
    'article_tag',
    Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True),
    Column('create_time', DATETIME, default=datetime.now)
)


# TODO: 1.先把两个需要做多对多的模型定义出来
# TODO: 创建Article模型
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)

    def __repr__(self):
        return '<Article(id={id}, title={title}, create_time={createTime})>'.format(id=self.id, title=self.title,
                                                                                    createTime=self.create_time)


# TODO: 创建Tag模型
class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)

    # TODO: 3.在两个需要做多对多的模型中随便选择一个模型，定义一个`relationship`属性，
    #   来绑定三者之间的关系，在使用`relationship`的时候，需要传入一个`secondary=中间表`
    articles = relationship('Article', backref='tags', secondary=article_tag)

    def __repr__(self):
        return '<Tag(id={id}, name={name}, create_time={createTime})>'.format(id=self.id, name=self.name,
                                                                              createTime=self.create_time)


# TODO: 删除数据表
# Base.metadata.drop_all()
# TODO: 重新创建数据表
# Base.metadata.create_all()

# TODO: 新增数据
# tag1 = Tag(name='python')
# tag2 = Tag(name='flask')
# article1 = Article(title='python基础语法')
# article2 = Article(title='flask基础语法')
#
# tag1.articles.append(article1)
# tag1.articles.append(article2)
# tag2.articles.append(article1)
# tag2.articles.append(article2)

# TODO: 提交数据
# session.add_all([tag1, tag2])
# session.commit()

# TODO: 2.根据文章查询文章所有标签
article = session.query(Article).first()
print('根据文章查询文章所有标签...')
print(article)
print(article.tags)

# TODO: 3.根据文章标签查询所有文章
tag = session.query(Tag).filter(Tag.id == 2).first()
print('根据文章标签查询所有文章...')
print(tag)
print(tag.articles)
