from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
# TODO: 设置秘钥
app.config['SECRET_KEY'] = os.urandom(24)
# TODO: 自定义session过期时间, 10天后过期
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=10)


@app.route('/')
def index():
    session['username'] = 'zhiliao'
    session['age'] = 20
    # TODO: 设置session有效期，默认31天后工期
    session.permanent = True
    return '设置session成功'


@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return username or '没有session数据'


@app.route('/del_session/')
def del_session():
    # TODO: 方式1
    # session.pop(key='username')
    # TODO: 方式2
    # del session['username']
    # TODO: 方式3删除全部session
    session.clear()
    return '删除session成功...'


if __name__ == '__main__':
    app.run(debug=True)
