# TODO: 产生循环引用
# from app import db

# TODO: 解决循环引用问题
from exts import db


# TODO: 定义User模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
