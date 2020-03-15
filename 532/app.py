from flask import Flask, render_template, g, abort

app = Flask(__name__)


@app.route('/')
def index():
    # print(g.username)
    abort(500)
    return render_template('index.html')


@app.route('/list/')
def myList():
    return render_template('list.html')


# TODO: errorhandler接收状态码，可以自定义返回这种状态码的响应的处理方法
@app.errorhandler(500)
def serverError(error):
    print('errorhandler钩子函数触发....')
    # return '服务器错误请稍后再试...', 500
    return render_template('500.html'), 500


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
