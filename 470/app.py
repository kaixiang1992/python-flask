from abc import ABC

from flask import Flask, views, url_for, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('list'))  # TODO: /list/
    return render_template('index.html')


# TODO：有几个url需要返回json数据
# 有几个视图，是需要返回相同的变量

class JSONView(views.View, ABC):
    def get_data(self):
        # TODO: 直接调用`JSONView`抛出未实现异常
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JSONView, ABC):
    def get_data(self):
        return {'username': 'zhiliao', 'age': 18, 'country': 'china'}


app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))


# TODO: 标准类视图继承父类`context`
class ADSView(views.View, ABC):
    def __init__(self):
        super(ADSView, self).__init__()
        self.context = {
            'abs': '今年过节不收礼，收礼只收脑白金'
        }


class LoginView(ADSView):
    def dispatch_request(self):
        self.context.update({
            'username': 'zhiliao'
        })
        return render_template('login.html', **self.context)


class RegisteredView(ADSView):
    def dispatch_request(self):
        return render_template('registered.html', **self.context)


app.add_url_rule('/login/', endpoint='login', view_func=LoginView.as_view('login'))
app.add_url_rule('/registered/', endpoint='registered', view_func=RegisteredView.as_view('registered'))


# with app.test_request_context():
#     print(url_for('list'))  # TODO: /list/

if __name__ == '__main__':
    app.run(debug=True)
