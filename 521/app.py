from flask import Flask, render_template, views, request
# TODO: 导入注册表单校验器
from validators.regist import RegistValidator
# TODO: 导入db对象及其配置项
from db.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from db.db import db
# TODO: 导入User模型
from models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app=app)


# TODO: 首页视图
@app.route('/')
def index():
    return render_template('index.html')


# TODO: 类视图
class RegistView(views.MethodView):
    def get(self):
        return render_template('regist.html')

    def post(self):
        form = RegistValidator(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            psd = form.psd.data
            money = form.money.data
            # print(email, username, psd, money)
            # TODO: 创建数据
            user = User(email=email, username=username, psd=psd, money=money)
            # TODO: 提交数据至数据库
            db.session.add(user)
            db.session.commit()
            return '注册成功...'
        else:
            print(form.errors)
            return '注册失败...'


# TODO: 添加类视图与URL的映射
app.add_url_rule(rule='/regist/', endpoint='regist', view_func=RegistView.as_view('regist'))

if __name__ == '__main__':
    app.run(debug=True)
