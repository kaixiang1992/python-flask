from flask_script import Manager
from app import app
from models import db
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app=app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
