from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# TODO: 1.创建数据库链接

# TODO: db_uri
# dialect+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/first_sqlalchemy_demo?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO: 2.创建ORM模型
# TODO: 定义User模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=Flask)
    create_time = db.Column(db.DATETIME, default=datetime.now)

    def __repr__(self):
        return '<User(name=%s)>' % self.name


# TODO: 定义Article模型
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_time = db.Column(db.DATETIME, default=datetime.now)

    authors = db.relationship('User', backref=db.backref('articles'), uselist=False)

    def __repr__(self):
        return '<Article(title=%s)>' % self.title


# TODO: 3.将ORM模型映射到数据库
# TODO: 3.1 创建测试数据
# TODO: TODO: 4.使用session提交数据
# db.drop_all()
# db.create_all()
# user1 = User(name='zhiliao')
# user2 = User(name='ketang')
# article1 = Article(title='title1')
# article2 = Article(title='title2')
# article3 = Article(title='title3')
# user1.articles.append(article1)
# user1.articles.append(article2)
# user2.articles.append(article3)
#
# db.session.add_all([user1, user2])
# db.session.commit()


# TODO: 5.查询数据
# user = User.query.all()
# print(user)  # TODO: [<User(name=zhiliao)>, <User(name=ketang)>]

user = User.query.first()
print(user.articles) # TODO: [<Article(title=title1)>, <Article(title=title2)>]


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
