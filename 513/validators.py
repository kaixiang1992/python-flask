from wtforms import Form, StringField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed


# TODO: 定义upload页面表单校验器
class UploadForm(Form):
    username = StringField(validators=[InputRequired(message='用户名不能为空')])
    """
    `flask_wtf.file.FileRequired`是用来验证文件上传是否为空。
    `flask_wtf.file.FileAllowed`用来验证上传的文件的后缀名。
    """
    avatar = FileField(validators=[FileRequired(), FileAllowed(upload_set=['jpg', 'png', 'gif'],
                                                               message="上传图片格式不符合要求")])
