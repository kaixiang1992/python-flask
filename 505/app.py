from flask import Flask
import config
# TODO: 产生循环引用
# from flask_sqlalchemy import SQLAlchemy
# TODO: 解决循环引用问题
from exts import db

from models import User

app = Flask(__name__)
app.config.from_object(config)

# TODO: 产生循环引用
# db = SQLAlchemy(app=app)

# TODO: 解决循环引用问题
db.init_app(app=app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/profile/')
def profile():
    pass


if __name__ == '__main__':
    app.run(debug=True)
