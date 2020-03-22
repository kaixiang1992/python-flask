from db import db
from datetime import datetime


# TODO: 定义用户模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)


# TODO: 定义标签模型
class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)


# TODO: 定义文章标签关联表
ArticleTags = db.Table('article_tag',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('create_time', db.DATETIME, default=datetime.now)
)


# TODO: 定义文章模型
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DATETIME, default=datetime.now)

    author = db.relationship('User', backref=db.backref('articles', uselist=True), uselist=False)
    tags = db.relationship('Tags', secondary=ArticleTags, backref=db.backref('articles', uselist=True), uselist=True)
