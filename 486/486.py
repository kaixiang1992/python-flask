from sqlalchemy import create_engine, Column, Integer, String, DATETIME, TEXT, and_, or_
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
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(11), nullable=False)
    price = Column(Integer, default=0, nullable=False)
    create_time = Column(DATETIME, default=datetime.now)
    context = Column(TEXT)

    def __repr__(self):
        return '<Article(title={title}, price={price})>'.format(title=self.title, price=self.price)


# TODO: 1.equals
result1 = session.query(Article).filter(Article.title == 'title0').first()
print(result1)

# TODO: 2.not equals
result2 = session.query(Article).filter(Article.title != 'title0').all()
print(result2)

# TODO: 3.like & ilike（不区分大小写）
# result3 = session.query(Article).filter(Article.title.like('title%')).all()
result3 = session.query(Article).filter(Article.title.ilike('title%')).all()
print(result3)

# TODO: 4.in
result4 = session.query(Article).filter(Article.title.in_(['title0', '苹果', '桃子'])).all()
print(result4)

# TODO: 5.not in
result5 = session.query(Article).filter(Article.title.notin_(['title0', '苹果', '桃子'])).all()
print(result5)

# TODO: 6.is null
result6 = session.query(Article).filter(Article.create_time == None).all()
print(result6)

# TODO: 7.is not null
result7 = session.query(Article).filter(Article.create_time != None).all()
print(result7)

# TODO: 8.and
# TODO: 8.1 传递多个参数
result8 = session.query(Article).filter(Article.title == '桃子', Article.context == '桃子').all()
print(result8)
# TODO: 8.2 使用and_函数
result9 = session.query(Article).filter(and_(Article.title == '桃子', Article.context == '桃子')).all()
print(result9)

# TODO: 9.or
result10 = session.query(Article).filter(or_(Article.title == '桃子', Article.context == '桃子')).all()
print(result10)
"""
SELECT article.id AS article_id, article.title AS article_title, article.price AS article_price, article.create_time AS article_create_time, article.context AS article_context 
FROM article 
WHERE article.title = %(title_1)s OR article.context = %(context_1)s
"""