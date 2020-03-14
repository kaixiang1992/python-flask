from flask import Flask, current_app, url_for

app = Flask(__name__)

# TODO: 应用上下文
# TODO: 第一种：手动推入app上下文
# app_context = app.app_context()
# app_context.push()
# print(current_app.name)  # TODO: app.py的文件名 => app

# TODO: 第二种：with方式
with app.app_context():
    print(current_app.name)  # TODO: app.py的文件名 => app


@app.route('/')
def hello_world():
    # print(current_app.name)  # TODO: app.py的文件名 => app

    # print(url_for('mylist'))    # TODO: /list/
    return 'Hello World!'


@app.route('/list/')
def mylist():
    return 'my list'


# TODO: 请求上下文
with app.test_request_context():
    print(url_for('mylist'))    # TODO: /list/


if __name__ == '__main__':
    app.run(debug=True)
