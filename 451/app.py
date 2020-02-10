from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/login/', methods=['GET', 'POST'])
@app.route('/account/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        next = request.args.get('next')
        print(next, username, password)
        return redirect(url_for(next, username=username, password=password), 302)


@app.route('/userprofile/<string:username>')
def user_profile(username):
    context = {
        'username': username,
        'password': request.args.get('password')
    }
    return render_template('userprofile.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
