from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # TODO: GET请求返回登录页面
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # TODO: 登录后重定向到个人中心页面
        username = request.form.get('username')
        if username:
            return redirect(url_for('profile', username=username), 302)
        else:
            return redirect(url_for('profile', username='无名氏'), 302)


@app.route('/profile/')
def profile():
    # TODO: 登录后显示登录昵称
    if request.args.get('username'):
        return '登录成功，当前用户：%s' % request.args.get('username')
    else:
        # TODO: 未登录重定向登录界面
        return redirect(url_for('login'), 302)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.31.176', port=8080)
