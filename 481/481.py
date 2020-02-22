from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

# TODO: 1.创建数据库引擎
engine = create_engine(DB_URI)

# TODO: 2.所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(engine)


# TODO: 3.1 创建一个ORM模型，这个ORM模型必须继承自sqlalchemy给我们提供好的基类
# TODO: 示例键`table`SQL:
# create table person(id int primary key autoincrement,name varchar(50),age int)

class Person(Base):
    # TODO: 定义表名
    __tablename__ = 'person'
    # TODO: 3.2. 在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射。这些属性必须是sqlalchemy给我们提供好的数据类型。
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(20))


# TODO: 4.将创建好的ORM模型，映射到数据库中。
Base.metadata.create_all()
