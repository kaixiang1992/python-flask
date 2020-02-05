from flask import Flask
import config

app = Flask(__name__)

# TODO: 2.app.debug = True

# TODO: 3.app.config.update(DEBUG=True)

# TODO: 4.app.config.from_object(config)
app.config.from_object(config)

"""
在Pycharm 2018以上版本中，开启DEBUG模式需要在pycharm右上角运行按钮左边的项目名称下，
选择Edit Configurations，打开编辑界面后，把FLASK_DEBU勾选上。

如果想要修改端口号和运行允许访问的ip地址，也是在编辑配置的界面中，在Additional options
中添加参数：--host=0.0.0.0 --port=8000

开启debug模式4中方法
1. 在执行`run`方法的时候，传递参数进去
app.run(debug=True)

2. 直接在应用对象设置
app.debug = True

3. 在`config`中设置
app.config.update(DEBUG=TRUE)

4.导入配置文件`config`
import config
app.config.from_object(config)
"""


@app.route('/')
def hello_world():
    # a = 1
    # b = 0
    # c = a / b
    # print(c)
    return 'Hello World!'


if __name__ == '__main__':
    # TODO: 1. app.run(debug=True)
    app.run()
