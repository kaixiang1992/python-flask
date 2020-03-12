import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@127.0.0.1:3300/csrf_demo?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)