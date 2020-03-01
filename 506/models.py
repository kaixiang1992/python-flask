from exts import db
from datetime import datetime


# TODO: 定义User模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    # TODO: 新增模型字段代码示例
    country = db.Column(db.String(50), nullable=False, default='china')
    areacode = db.Column(db.Integer, nullable=False, default=86)

