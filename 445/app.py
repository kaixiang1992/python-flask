from flask import Flask, url_for
from customConverter import telConverter, ListConverter

app = Flask(__name__)
app.url_map.converters['tel'] = telConverter
app.url_map.converters['list'] = ListConverter


@app.route('/')
def hello_world():
    print(url_for('posts', boards=['a', 'b']))
    return 'Hello World!'


# TODO: /user/123
@app.route('/user/<string:user_id>')
def user_profile(user_id):
    return '您输入的user id 是：%s' % user_id


# TODO: http://127.0.0.1:5000/telphone/13077891234
@app.route('/telphone/<tel:tel>')
def my_tel(tel):
    return '您的手机号码是：%s' % tel


@app.route('/post/<list:boards>')
def posts(boards):
    # print(boards)
    # boards = boards.split('+')
    return '您提交的模板是：%s' % boards


if __name__ == '__main__':
    app.run(debug=True)
