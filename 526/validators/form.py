from wtforms import Form, StringField, FloatField
from wtforms.validators import InputRequired, Length, EqualTo, Email


# TODO: 注册表单校验器
class RegistValidator(Form):
    email = StringField(validators=[InputRequired(message='邮箱不能为空'), Email(message='邮箱输入错误格式不符')])
    username = StringField(validators=[InputRequired(message='用户名不能为空'),
                                       Length(min=3, max=10, message='用户名为3-10位字符串')])
    psd = StringField(validators=[InputRequired(message='密码不能为空'),
                                  Length(min=3, max=10, message='密码为3-10位字符串')])
    psd_repeat = StringField(validators=[InputRequired('密码不能为空'),
                                         EqualTo(fieldname='psd', message='两次密码输入不一致')])
    money = FloatField(validators=[InputRequired(message='账户金额不能为空')])


# TODO: 登录表单校验器
class LoginValidator(Form):
    email = StringField(validators=[InputRequired(message='邮箱不能为空'), Email(message='邮箱输入错误格式不符')])
    psd = StringField(validators=[InputRequired(message='密码不能为空'),
                                  Length(min=3, max=10, message='密码为3-10位字符串')])


# TODO: 转账表单检验器
class TransferValidator(Form):
    email = StringField(validators=[InputRequired(message='邮箱不能为空'), Email(message='邮箱输入错误格式不符')])
    money = FloatField(validators=[InputRequired(message='账户金额不能为空')])
