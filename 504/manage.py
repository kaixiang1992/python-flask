from flask_script import Manager
from app import app
# TODO: 通过`manager.add_command`来添加
from db_manage import db_manage

manage = Manager(app=app)
# TODO: 通过`manager.add_command`来添加
"""
manage.add_command(param1, param2)
param1: 命令前缀名，如: db
param2: Manager对象，如：导入进来的db_manage
"""
manage.add_command('db', db_manage)

# TODO: 命令: python manage.py greet
@manage.command
def greet():
    print('你好....')


@manage.option('-u', '--username', dest='username')
@manage.option('-a', '--age', dest="age")
def welcome(username, age):
    print('输入的姓名: %s，输入的年纪：%s' % (username, age))


if __name__ == '__main__':
    manage.run()
