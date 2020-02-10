from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'position': -9
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
