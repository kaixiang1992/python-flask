from flask import Flask, views, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


class LoginView(views.MethodView):
    def __render(self, **context):
        return render_template('login.html', **context)

    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        userpsd = request.form.get('userpsd')
        print(username, userpsd)
        if username == 'admin' and userpsd == 'admin123':
            return '登录成功'
        else:
            return self.__render(error="用户名或密码错误")


app.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))


if __name__ == '__main__':
    app.run(debug=True)
