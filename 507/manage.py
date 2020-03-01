from flask_script import Manager
from app import app
from exts import db
from flask_migrate import Migrate, MigrateCommand
# TODO: 需要把映射到数据库中的模型导入到manage.py文件中
from models import User

manage = Manager(app=app)
migrate = Migrate(app=app, db=db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()