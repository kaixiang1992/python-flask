from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'username': 'kaixiang'
    }
    return render_template('index.html', **context)


@app.route('/detail/')
def details():
    return render_template('detail.html')


if __name__ == '__main__':
    app.run(debug=True)
