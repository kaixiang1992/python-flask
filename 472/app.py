from flask import Flask, views, request
from functools import wraps

app = Flask(__name__)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        print(username)
        if username == 'zhiliao':
            return func(*args, **kwargs)
        else:
            return '请先登录'

    return wrapper


@app.route('/')
def index():
    return '首页'


# TODO: 函数视图装饰器正确示例
# TODO: app.route('/my/')(login_required(my)(*args, **kwargs))  ==> 正确示例
@app.route('/my/')
@login_required
def my():
    return '我的主页'


# TODO: 函数视图装饰器错误示例
# TODO: http://127.0.0.1:5000/my/  ==> 依旧返回  `我的主页`
# TODO: login_required(app.route('/my/')(my)(*args, **kwargs))  ==> 错误示例
# @login_required
# @app.route('/my/')
# def my():
#     return '我的主页'


# TODO: 类视图装饰器
class setting(views.View):
    """
    TODO: 列表或者元组都可以，里面装的就是所有的装饰器
    """
    # decorators = [login_required]
    decorators = (login_required, )

    def dispatch_request(self):
        return '我的设置'


app.add_url_rule('/setting/', endpoint='setting', view_func=setting.as_view('setting'))

if __name__ == '__main__':
    app.run(debug=True)
