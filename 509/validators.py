from wtforms import Form, StringField, IntegerField
from wtforms.validators import Email, InputRequired, NumberRange, Length, Regexp, URL, UUID


# TODO: 定义登录页面表单校验器
class LoginForm(Form):
    # TODO: 1.Email：验证上传的数据是否为邮箱。
    email = StringField(validators=[Email(message='邮箱格式错误')])
    # TODO: 2.InputRequir：原始数据的需要验证。如果不是特殊情况，应该使用InputRequired。
    username = StringField(validators=[InputRequired(message='username不能传为空')])
    # TODO: 3.NumberRange：数字的区间，有min和max两个值限制，如果处在这两个数字之间则满足。
    age = IntegerField(validators=[NumberRange(min=12, max=100, message='有效年纪为：12-100岁')])
    # TODO: 4.Regexp：自定义正则表达式
    phone = StringField(validators=[Length(min=11, max=11, message='手机号为11位数字'),
                                    Regexp(regex=r'1[356789]\d{9}', message='手机号格式输入有误')])
    # TODO: 5.URL：必须要是URL的形式
    homepage = StringField(validators=[URL(message='URL格式输入有误...')])
    # TODO: 6.UUID：验证UUID
    uuidstr = StringField(validators=[UUID(message='uuid格式有误...')])
