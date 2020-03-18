from flask import Flask, url_for, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
# TODO: 1.创建一个`api`对象
api = Api(app)


# TODO: 2.继承自`Resource`
# TODO: 只能采用`post`请求，那么就定义一个`post`方法
class LoginView(Resource):
    def post(self, username=None):
        return {"username":username}


# TODO: 3.使用`api.add_resource`来添加视图与`url`
api.add_resource(LoginView, '/login/<string:username>/', '/registered/<string:username>/', endpoint="login")


# TODO: 使用endpoint反转URL
with app.test_request_context():
    print(url_for(endpoint='login', username="zhiliao"))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
