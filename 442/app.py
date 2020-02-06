from flask import Flask
# TODO: 1. import config

app = Flask(__name__)
# TODO: 1. app.config.from_object(config)

# TODO: 2. app.config.from_pyfile('./config.py')
app.config.from_pyfile('./config.txt')

"""
1.如果项目的配置特别多，可以把所有的配置项都放置在一个模块中，然后通过加载的方式进行配置
示例：通过模块对象
import config
app.config.from_object(config)

2.另一个加载方法`app.config.from_pyfile()`，该方法传入一个文件名，通常是以`.py`结尾的文件
但也不限于只使用`.py`后缀的文件，如`config.txt`。
silent=False, 参数默认为`False`如果配置文件不存在，则抛出异常
silent=True，如果配置文件不存在不会抛出异常
app.config.from_pyfile('./config.py')
app.config.from_pyfile('./config.txt')
"""


@app.route('/')
def hello_world():
    # print(1/0)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
