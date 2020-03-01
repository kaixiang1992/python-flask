from flask_script import Manager
from app import db, BackendUser

db_manage = Manager()


@db_manage.command
def init():
    print('alembic init alembic成功...')


@db_manage.command
def revision():
    print('alembic revision --autogenerate -m "message" 成功....')


@db_manage.command
def upgrade():
    print('alembic upgrade head 成功....')


@db_manage.option('-u', '--username', dest="username")
@db_manage.option('-e', '--email', dest='email')
def add_user(username, email):
    user = BackendUser(name=username, email=email)
    db.session.add(user)
    db.session.commit()