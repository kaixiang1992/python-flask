from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


# TODO: 定义User模型
class BackendUser(db.Model):
    __tablename__ = 'backend_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
