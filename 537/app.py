from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, inputs
from datetime import date

app = Flask(__name__)
api = Api(app)


class LoginView(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        # TODO: 1.default：默认值，如果这个参数没有值，那么将使用这个参数指定的值。
        parse.add_argument('country', default="china")
        # TODO: 2.required：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。
        parse.add_argument('username', type=str, help='请输入用户名', required=True)
        # TODO: 3.type：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。
        parse.add_argument('age', type=int, help="输入年纪格式不符", required=True)
        # TODO: 4.choices：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。
        parse.add_argument('gender', type=str, choices=['male', 'female', 'secret'], help="提交的性别不符", required=True)
        # TODO: 6.trim：是否要去掉前后的空格。
        parse.add_argument('address', type=str, trim=True, help='请输入地址', required=True)

        # TODO: 1.url：会判断这个参数的值是否是一个url，如果不是，那么就会抛出异常。
        parse.add_argument('homepage', type=inputs.url, help='主页地址输入错误', required=True)
        # TODO: 2.regex：正则表达式。
        parse.add_argument('phone', type=inputs.regex(r'1[356789]\d{9}'), help="手机号输入错误", required=True)
        # TODO: 3.date：将这个字符串转换为datetime.date数据类型。如果转换不成功，则会抛出一个异常。
        parse.add_argument('create_time', type=inputs.date, help='日期输入格式有误', required=True)

        args = parse.parse_args()
        print(args)
        return {"username": "zhiliao"}


api.add_resource(LoginView, '/login/', endpoint="login")


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
