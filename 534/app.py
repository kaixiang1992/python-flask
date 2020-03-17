from flask import Flask, render_template, template_rendered, got_request_exception

app = Flask(__name__)


# TODO: 1.template_rendered：模版渲染完成后的信号。
def template_rendered_func(sender, template, context):
    # TODO: <Flask 'app'>
    print(sender)
    # TODO: <Template 'index.html'>
    print(template)
    # TODO: {'g': <flask.g of 'app'>, 'request': <Request 'http://127.0.0.1:5000/' [GET]>, 'session': <NullSession {}>}
    print(context)


template_rendered.connect(template_rendered_func)


# TODO: 2.got_request_exception：视图函数发生异常的信号
def got_request_exeption_func(sender, exeption):
    print(sender)
    print(exeption)


got_request_exception.connect(got_request_exeption_func)


@app.route('/')
def index():
    a = 1 / 0
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
