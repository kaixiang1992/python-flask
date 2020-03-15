from flask import Flask, request, g
from blinkers import login_signal

app = Flask(__name__)


@app.route('/')
def index():
    username = request.args.get('username')
    if username:
        g.username = username
        # TODO: 3.发送信号
        # login_signal.send(username=username)
        login_signal.send()
        return '登录成功'
    else:
        return '请先登录'


if __name__ == '__main__':
    app.run(debug=True)
