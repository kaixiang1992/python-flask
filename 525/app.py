from flask import Flask, render_template, views, request, session
# TODO: 导入注册表单校验器
from validators.form import RegistValidator, LoginValidator, TransferValidator
# TODO: 导入db对象及其配置项
from db.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SECRET_KEY
from db.db import db
# TODO: 导入User模型
from models.user import User
# TODO: 登录拦截器
from auth import login_required
# TODO: 防止CSRF攻击
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = SECRET_KEY
# TODO: 防止CSRF攻击
CSRFProtect(app=app)

db.init_app(app=app)


# TODO: 首页视图
@app.route('/')
def index():
    return render_template('index.html')


# TODO: 注册类视图
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


# TODO: 登录类视图
class LoginView(views.MethodView):

    def get(self):
        return render_template('login.html')

    def post(self):
        form = LoginValidator(request.form)
        if form.validate():
            email = form.email.data
            psd = form.psd.data
            user = User.query.filter(User.email == email, User.psd == psd).first()
            if user:
                # TODO: 登录成功存储user.id到session中
                session['user_id'] = user.id
                # TODO: 当前csrf_token
                print(session.get('csrf_token'))    # TODO: 2eaafe1a4914d304244564be7844f76f8b4d558c
                return '登录成功...'
            else:
                return '账号或密码错误...'
        else:
            print(form.errors)
            return '登录失败...'


# TODO: 转账类视图
class TransferView(views.MethodView):
    # TODO: 使用登录拦截装饰器
    decorators = [login_required]

    def get(self):
        return render_template('transfer.html')

    def post(self):
        form = TransferValidator(request.form)
        if form.validate():
            email = form.email.data
            money = form.money.data
            user = User.query.filter(User.email == email).first()
            if user:
                myself = User.query.filter(User.id == session.get('user_id')).first()
                if myself:
                    # TODO: 余额充足发起转账
                    if myself.money > money:
                        myself.money -= money
                        user.money += money
                        db.session.commit()
                        return '转账成功...'
                    else:
                        return '账户余额不足...'
                else:
                    return '转账失败请登录...'
            else:
                return '收款人不存在...'
        else:
            return '转账失败...'


# TODO: 添加类视图与URL的映射
app.add_url_rule(rule='/regist/', endpoint='regist', view_func=RegistView.as_view('regist'))
app.add_url_rule(rule='/login/', endpoint='login', view_func=LoginView.as_view('login'))
app.add_url_rule(rule='/transfer/', endpoint='transfer', view_func=TransferView.as_view('transfer'))

if __name__ == '__main__':
    app.run(debug=True)
