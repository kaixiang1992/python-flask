# TODO: 从flask框架中导入Flask类
from flask import Flask

# TODO: 传入`__name__`初始化一个实例
app = Flask(__name__)


# TODO: app.route装饰器映射URL和执行的函数。这个设置将URL映射到了hello_world函数上
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/list')
def my_list():
    return 'my list'


if __name__ == '__main__':
    # TODO: 运行本项目默认的`host`是`127.0.0.1`, `port`端口是`5000`，port参数更改默认`5000`端口
    app.run(port=8080, debug=True)
