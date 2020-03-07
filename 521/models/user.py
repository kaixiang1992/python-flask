import os
import sys
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from db.db import db


# TODO: 定义User模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    psd = db.Column(db.String(30), nullable=False)
    money = db.Column(db.Float, nullable=False, default=0)
    create_time = db.Column(db.DATETIME, default=datetime.now)
