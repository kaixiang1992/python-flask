from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

# TODO: 创建数据库引擎
engine = create_engine(DB_URI)

# TODO: 所有的类都要继承自`declarative_base`这个函数生成的基类
Base = declarative_base(bind=engine)

# TODO: 构建`session`对象
session = sessionmaker(bind=engine)()


# TODO: 创建`Person`ORM模型
# create table person(id int primary key autoincrement,name varchar(50),age int)
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)

    def __str__(self):
        return '<Person(id={id}, name={name}, age={age})>'.format(id=self.id, name=self.name, age=self.age)


# TODO: 添加数据
def add_person():
    # TODO: 提交一条数据
    # p = Person(name='zhiliao', age=18)
    # session.add(p)
    # session.commit()
    # TODO: 一次性提交多条数据
    p1 = Person(name='zhiliao1', age=19)
    p2 = Person(name='zhiliao2', age=20)
    session.add_all([p1, p2])
    session.commit()


# TODO: 查询数据
def query_person():
    # TODO: 查找某个模型对应的那个表中所有的数据
    # all_person = session.query(Person).all()
    # for x in all_person:
    #     print(x)

    # TODO: 使用filter_by来做条件查询
    # all_person = session.query(Person).filter_by(name='zhiliao').all()
    # for x in all_person:
    #     print(x)

    # TODO: 使用filter来做条件查询
    # all_person = session.query(Person).filter(Person.name=='zhiliao').all()
    # for x in all_person:
    #     print(x)

    # TODO: 使用get方法查找数据，get方法是根据primary_key(当前数据列为=id)来查找的，只会返回一条数据或者None
    # all_person = session.query(Person).get(1)
    # print(all_person)  # TODO: <Person(id=1, name=zhiliao, age=18)>
    # all_person = session.query(Person).get(100)
    # print(all_person)  # TODO: None

    # TODO: 使用first方法获取结果集中的第一条数据
    all_persion = session.query(Person).first()
    print(all_persion)  # TODO: <Person(id=1, name=zhiliao, age=18)>


# TODO: 修改数据
def update_person():
    p1 = session.query(Person).first()
    p1.name = 'ketang'
    session.commit()


# TODO: 删除数据
def delete_person():
    p1 = session.query(Person).first()
    print(p1)  # TODO: <Person(id=1, name=ketang, age=18)>
    session.delete(p1)
    session.commit()


if __name__ == '__main__':
    # add_person()  # TODO: 添加数据
    # query_person()  # TODO: 查询数据
    # update_person()  # TODO: 修改数据
    delete_person()  # TODO: 删除数据
