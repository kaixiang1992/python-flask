from sqlalchemy import create_engine, Column, Integer, Float, Boolean, DECIMAL, Enum, Date, DATETIME, TIME, TEXT
from sqlalchemy.dialects.mysql import LONGTEXT, DOUBLE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# TODO: python3 枚举实现
import enum

from datetime import date, datetime, time

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)

session = sessionmaker(bind=engine)()


# TODO:  python3 枚举实现
class Entag(enum.Enum):
    javascript = 'javascript'
    html = 'html'
    css = 'css'


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # TODO: 2.浮点类型 -- 小数点后4位精度
    price = Column(Float)

    # TODO: 3.Boolean：传递True/False进去
    is_delete = Column(Boolean)

    # TODO: 4.DECIMAL：定点类型。是专门为了解决浮点类型精度丢失的问题的。在存储钱相关的字段的时候建议大家都使用这个数据类型。
    #  并且这个类型使用的时候需要传递两个参数，第一个参数是用来标记这个字段总能能存储多少个数字，第二个参数表示小数点后有多少位。
    dec_price = Column(DECIMAL(10, 4))

    # TODO: 5.Enum：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用Enum来作为枚举 -- python2
    tag_py2 = Column(Enum('python', 'flask', 'django'))

    # TODO: 5.Enum：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用Enum来作为枚举 -- python3
    tag_py3 = Column(Enum(Entag))

    # TODO: 6.Date：存储时间，只能存储年月日。映射到数据库中是date类型。在Python代码中，可以使用`datetime.date`来指定
    create_date = Column(Date)

    # TODO: 7.DateTime：存储时间，可以存储年月日时分秒毫秒等。映射到数据库中也是datetime类型。在Python代码中，可以使用`datetime.datetime`来指定
    create_datetime = Column(DATETIME)

    # TODO: 8.Time：存储时间，可以存储时分秒。映射到数据库中也是time类型。在Python代码中，可以使用`datetime.time`来至此那个
    create_time = Column(TIME)

    # TODO: 9.Text：存储长字符串。一般可以存储6W多个字符。如果超出了这个范围，可以使用LONGTEXT类型。映射到数据库中就是text类型。
    context_text = Column(TEXT)

    # TODO: 10.LONGTEXT：长文本类型，映射到数据库中是longtext类型。
    context_longtext = Column(LONGTEXT)


# TODO: 删除数据库
Base.metadata.drop_all()
# TODO: 新建数据库
Base.metadata.create_all()

# TODO: 2.浮点类型 -- 小数点后4位精度
article = Article(price=10.123456)
session.add(article)

# TODO: 3.Boolean：传递True/False进去
article1 = Article(is_delete=True)
session.add(article1)

# TODO: 4.DECIMAL：定点类型。是专门为了解决浮点类型精度丢失的问题的。在存储钱相关的字段的时候建议大家都使用这个数据类型。
#  并且这个类型使用的时候需要传递两个参数，第一个参数是用来标记这个字段总能能存储多少个数字，第二个参数表示小数点后有多少位。
article2 = Article(dec_price=999999.9999)
session.add(article2)

# TODO: 5.Enum：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用Enum来作为枚举 -- python2
article3 = Article(tag_py2='flask')
session.add(article3)

# TODO: 5.Enum：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用Enum来作为枚举 -- python3
article4 = Article(tag_py3='html')
session.add(article4)

# TODO: 6.Date：存储时间，只能存储年月日。映射到数据库中是date类型。在Python代码中，可以使用`datetime.date`来指定
article5 = Article(create_date=date(2020, 2, 23))
session.add(article5)

# TODO: 7.DateTime：存储时间，可以存储年月日时分秒毫秒等。映射到数据库中也是datetime类型。在Python代码中，可以使用`datetime.datetime`来指定
article6 = Article(create_datetime=datetime(2020, 2, 23, 0, 19))
session.add(article6)

# TODO: 8.Time：存储时间，可以存储时分秒。映射到数据库中也是time类型。在Python代码中，可以使用`datetime.time`来至此那个
article7 = Article(create_time=time(0, 22, 12))
session.add(article7)

# TODO: 9.Text：存储长字符串。一般可以存储6W多个字符。如果超出了这个范围，可以使用LONGTEXT类型。映射到数据库中就是text类型。
article8 = Article(context_text='一闪一闪亮晶晶')
session.add(article8)

# TODO: 10.LONGTEXT：长文本类型，映射到数据库中是longtext类型。
article9 = Article(context_longtext='一闪一闪亮晶晶一闪一闪亮晶晶一闪一闪亮晶晶一闪一闪亮晶晶一闪一闪亮晶晶...')
session.add(article9)

# TODO: 提交数据
session.commit()
