from flask_script import Manager
from app import app
from models import db
from flask_migrate import Migrate, MigrateCommand

manage = Manager(app=app)
migrate = Migrate(app=app, db=db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()