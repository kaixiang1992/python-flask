from sqlalchemy import create_engine, Integer, String, Column, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    city = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return '<User(name=%s, city=%s, age=%s)>' % (self.name, self.city, self.age)


# TODO: 1.删除数据表，创建数据表
# TODO: 2.创建测试数据
# TODO: 3.提交数据
# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# user1 = User(name='李A', city='长沙', age=18)
# user2 = User(name='张B', city='北京', age=19)
# user3 = User(name='王C', city='长沙', age=18)
# user4 = User(name='赵D', city='长沙', age=20)
#
# session.add_all([user1, user2, user3, user4])
# session.commit()

# TODO: select user.name, user.city, user.age from user,(select user.city, user.age from user where user.name='李A')
#  as stmt where user.city=stmt.city and user.age=stmt.age;
#  TODO: 1.基础实现
# stmt = session.query(User).filter(User.name == '李A').first()
# users = session.query(User).filter(User.city == stmt.city, User.age == stmt.age).all()
# print(users)    # TODO: [<User(name=李A, city=长沙, age=18)>, <User(name=王C, city=长沙, age=18)>]


# TODO: 2.subquery示例
stmt = session.query(User.city.label('city'), User.age.label('age')).filter(User.name == '李A').subquery()
users = session.query(User.name, User.city, User.age).filter(User.city == stmt.c.city, User.age == stmt.c.age).all()
print(users)    # TODO: [('李A', '长沙', 18), ('王C', '长沙', 18)]
