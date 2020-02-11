from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'text': 'hello zhiliao, hello ketang'
    }
    return render_template('index.html', **context)


@app.template_filter('cut')
def cut(value):
    value = value.replace('hello', 'welcome')
    return value


if __name__ == '__main__':
    app.run()
