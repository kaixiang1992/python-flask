from werkzeug.routing import BaseConverter


# TODO: /telphone/13077891234
# TODO: 一个URL中，含有手机号码的变量，必须限定这个变量的字符串格式满足手机号码的格式
class telConverter(BaseConverter):
    regex = r'1[356789]\d{9}'


# TODO: 用户访问http://127.0.0.1:5000/post/a+b
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        # print('*' * 30)
        # print(value)
        # print('*' * 30)
        return '+'.join(value)
