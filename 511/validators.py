from wtforms import Form, StringField, BooleanField, SelectField, IntegerField
from wtforms.validators import Length, InputRequired, NumberRange


# TODO: 定义setting页面表单校验器
class SettingForm(Form):
    username = StringField(label='用户名', validators=[InputRequired(message='username不能为空')])
    age = IntegerField(label='年龄', validators=[NumberRange(min=12, max=100)])
    remember = BooleanField(label='记住我?', validators=[InputRequired()])
    tags = SelectField(label='标签', validators=[InputRequired()], choices=[('1', 'python'), ('2', 'javascript'),
                                                                          ('3', 'php')])
