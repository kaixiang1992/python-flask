from sqlalchemy import create_engine, Column, Integer, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/alembic_demo?charset=utf8'

engine = create_engine(DB_URI)

Base = declarative_base(bind=engine)


# TODO: 定义User模型
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    # TODO: 增加字段
    age = Column(Integer, nullable=False)
    country = Column(String(50), nullable=False)
    create_time = Column(DATETIME, default=datetime.now)
