from flask import Flask, Response, request
from blueprint.cms import cms

app = Flask(__name__)
app.config['SERVER_NAME'] = 'testflask.com:5000'
app.register_blueprint(cms)


@app.route('/')
def index():
    res = Response(response='设置主域名cookie')
    res.set_cookie(key='username', value='zhiliao', max_age=3600, domain=".testflask.com")
    return res


@app.route('/profile/')
def profile():
    username = request.cookies.get(key='username')  # TODO: zhiliao
    return '读取到的cookie信息为：%s' % username


if __name__ == '__main__':
    app.run(debug=True)
