from flask import Flask, render_template, request
from validators import LoginForm

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return 'success...'
        else:
            print(form.errors)
            return 'fail...'


if __name__ == '__main__':
    app.run()
