from flask import Flask, g, request, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def index():
    username = request.args.get('username')
    if username:
        session['user_id'] = 1
    return 'Hello World!'


@app.route('/profile/')
def profile():
    if hasattr(g, 'username'):
        return g.username
    else:
        return '没有缓存用户信息...'


# TODO: before_first_request：处理第一次请求之前执行
@app.before_first_request
def first_request():
    print('处理第一次请求之前执行....')


# TODO: before_request：在每次请求之前执行
@app.before_request
def beforeRequest():
    if session.get('user_id'):
        g.username = 'zhiliao'
    print('在每次进入视图函数之前执行...')


if __name__ == '__main__':
    app.run(debug=True)
