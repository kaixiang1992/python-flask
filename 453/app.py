from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'position': -9,
        # 'signature': '我就是我不一样的烟火'
        'signature': []
        # 'signature': '' or '我就是我不一样的烟火'
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
