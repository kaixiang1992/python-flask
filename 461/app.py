from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'username': 'zhiliao'
    }
    return render_template('index/index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
