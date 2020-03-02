from wtforms import Form, StringField
from wtforms.validators import Length, Regexp, ValidationError


# TODO: 定义登录页面表单校验器
class LoginForm(Form):
    code = StringField(validators=[Length(min=4, max=4, message='验证码格式为4位字符串'),
                                   Regexp(regex=r'\d{4}', message="验证码为4位数字")])

    def validate_code(self, filed):
        # print(type(filed))  # TODO: <class 'wtforms.fields.core.StringField'>
        print(filed.data)
        if filed.data != '1234':
            raise ValidationError('验证码输入错误...')

