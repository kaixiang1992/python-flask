from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'username': 'zhiliao',
        'age': 18,
        'country': 'china',
        'childrens': {
            'name': 'ketang',
            'height': 170
        }
    }

    # return render_template('index.html', username='zhiliao', age=18, country='china')
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.31.176', port=8080)
