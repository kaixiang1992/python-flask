from flask import Flask, url_for

app = Flask(__name__)

"""
app.route装饰器执行方式：
1.执行`app.route(rule, **options)`返回：decorator函数体

2.相当于执行：`decorator(hello_world)`，执行函数体中包含以下代码：
self.add_url_rule(rule, endpoint, f, **options)。实则调用方式如3

3.app.add_url_rule(rule, endpoint=None, view_func=None, **options)
"""


@app.route('/')
def hello_world():
    # TODO: 使用了`endpoint`
    print(url_for('list'))  # TODO: /list/
    # TODO: 未使用`endpoint`
    print(url_for('detail'))  # TODO: /detail/
    return 'Hello World!'


def my_list():
    return '我的列表'


def detail():
    return '我的详情'


app.add_url_rule('/list/', endpoint='list', view_func=my_list)
app.add_url_rule('/detail/', view_func=detail)

if __name__ == '__main__':
    app.run(debug=True)
