from flask import Flask, render_template, request
from validators import LoginForm
from uuid import uuid4

app = Flask(__name__)

print(uuid4())


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
    app.run(debug=True)
