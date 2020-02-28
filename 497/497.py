from sqlalchemy import create_engine, Column, Integer, String, DATETIME, Enum, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

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
    age = Column(Integer, nullable=False)
    # TODO: 枚举 ---> 性别
    # TODO: "male","female","secret"  => 男性、女性、秘密
    gender = Column(Enum("male", "female", "secret"), default="secret")
    create_time = Column(DATETIME, default=datetime.now)


# TODO: 删除数据表
# Base.metadata.drop_all()
# TODO: 创建数据表
# Base.metadata.create_all()

# TODO: 创建数据
# user1 = User(name='张三', age=17, gender='male')
# user2 = User(name='李四', age=17, gender='male')
# user3 = User(name='王武', age=18, gender='male')
# user4 = User(name='赵敏', age=19, gender='female')
# user5 = User(name='周芷若', age=20, gender='female')

# TODO: 提交数据
# session.add_all([user1, user2, user3, user4, user5])
# # session.commit()


# TODO: 1.group_by
# TODO: 以User.age进行分组
# user_group = session.query(User.age, func.count(User.id)).group_by(User.age).all()
# print(user_group)   # TODO: [(17, 2), (18, 1), (19, 1), (20, 1)]

# TODO: 2.having
# TODO: 以User.age进行分组，然后在对分组进行过滤未成年人
user_group = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 18).all()
print(user_group)   # TODO: [(17, 2)]
