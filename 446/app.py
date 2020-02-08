from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/list/', methods=['POST'])
def my_list():
    return 'My List!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'login success'


if __name__ == '__main__':
    app.run(debug=True, host='192.168.31.176', port=8080)
