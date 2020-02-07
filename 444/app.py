from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    # /list/1
    # /list/2
    # print(url_for('my_list', page=1, count=10))   #TODO: /list/1?count=10
    # return 'Hello World!'
    # return url_for('my_list', page=1, count=10)
    # return url_for('detail', id=1)  # TODO: /post/detail/1
    return url_for('login', next='/')  # TODO: /login?next=%2F


@app.route('/login')
def login():
    next_url = request.args.get('next')
    print(next_url)
    return 'login page'


# TODO: http://127.0.0.1:5000/list/2
@app.route('/post/list/<int:page>')
def my_list(page):
    return 'my list page %s' % page


@app.route('/post/detail/<int:id>')
def detail(id):
    return 'detail'


if __name__ == '__main__':
    app.run(debug=True)
