from flask import Flask, request, g, render_template

app = Flask(__name__)


@app.route('/')
def index():
    username = request.args.get('username')
    if username:
        g.username = username
    return render_template('index.html')


@app.route('/profile/')
def profile():
    return render_template('profile.html')


# TODO: context_processor：上下文处理器。返回的字典中的键可以在模板上下文中使用
@app.context_processor
def contextProcessor():
    print('上下文处理器...')
    print(hasattr(g, 'username'))
    if hasattr(g, 'username'):
        return {'username': g.username}
    else:
        return {}


if __name__ == '__main__':
    app.run(debug=True)
