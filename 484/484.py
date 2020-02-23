from sqlalchemy import create_engine, Integer, Column, DATETIME, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


class Article(Base):
    __tablename__ = 'article'
    # TODO: 1.primary_key：设置某个字段为主键。
    # TODO: 2.autoincrement：设置这个字段为自动增长的。
    id = Column(Integer, primary_key=True, autoincrement=True)

    # TODO: 3.default：设置某个字段的默认值。在发表时间这些字段上面经常用。
    create_time = Column(DATETIME, default=datetime.now)

    # TODO: 4.nullable：指定某个字段是否为空。默认值是True，就是可以为空。
    title = Column(String(50), nullable=False)

    # TODO: 5.unique：指定某个字段的值是否唯一。默认是False
    phone = Column(String(11), unique=True)

    # TODO: 6.onupdate：在数据更新的时候会调用这个参数指定的值或者函数。在第一次插入这条数据的时候，不会用onupdate的值，
    #  只会使用default的值。常用的就是update_time（每次更新数据的时候都要更新的值）
    update_time = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    # TODO: 7.name：指定ORM模型中某个属性映射到表中的字段名。如果不指定，那么会使用这个属性的名字来作为字段名。
    #  如果指定了，就会使用指定的这个值作为参数。这个参数也可以当作位置参数，在第1个参数来指定。
    desc = Column(String(20), name='user_desc')


# TODO: 删除数据库
Base.metadata.drop_all()
# TODO: 创建数据库
Base.metadata.create_all()

# TODO: 4.nullable：指定某个字段是否为空。默认值是True，就是可以为空。
article = Article(title='测试文章')
session.add(article)

# TODO: 5.unique：指定某个字段的值是否唯一。默认是False
# article1 = Article(title='测试是否唯一', phone='18888888888')
# article2 = Article(title='测试是否唯一', phone='18888888888')
# session.add_all([article1, article2])
# session.add(article1)

# TODO: 6.onupdate：在数据更新的时候会调用这个参数指定的值或者函数。
# article1 = session.query(Article).first()
# article1.title = '更改测试文章'
# session.add(article1)

# TODO: 提交保存
session.commit()
