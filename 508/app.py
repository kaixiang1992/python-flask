from flask import Flask, render_template, url_for, request, jsonify
from wtforms import Form, StringField
from wtforms.validators import Length, EqualTo

app = Flask(__name__)


# TODO: 定义注册表单校验器
class RegisterForm(Form):
    username = StringField(validators=[Length(min=4, max=10, message='用户昵称为4-10位字符.')])
    password = StringField(validators=[Length(min=6, max=10, message='密码为6-10位字符')])
    repeat_password = StringField(validators=[Length(min=6, max=10, message='二次密码为6-10位字符串'),
                                              EqualTo('password', message='两次密码输入不一致')])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # TODO: 检验用户输入结果
        form = RegisterForm(request.form)
        # TODO: 返回校验结果，Boolean类型
        print(form.validate())
        if form.validate():  # TODO: 检验成功
            return '注册成功!'
        else:  # TODO: 检验失败
            print(form.errors)  # TODO: 错误信息
            return 'fail'


if __name__ == '__main__':
    app.run(debug=True)
