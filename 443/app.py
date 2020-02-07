from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# TODO: http://127.0.0.1:5000/article
@app.route('/article')
def article_list():
    return 'article list'


# TODO: string类型
# TODO: http://127.0.0.1:5000/article/c75776gnnb
# TODO: 不能接受带斜杠路径：http://127.0.0.1:5000/article/c75776gnnb/ahghgh123
@app.route('/article/<article_id>')
def article_detail(article_id):
    return 'article detail by %s' % (article_id,)


# TODO: int类型
# TODO: http://127.0.0.1:5000/p/100
# TODO: 不能接受非`int`类型：http://127.0.0.1:5000/p/1001.123
@app.route('/p/<int:project_id>')
def project_detail(project_id):
    return 'project detail by id=%s' % (project_id)


# TODO: float类型
# TODO: http://127.0.0.1:5000/project/100.123
# TODO: 不能接受非`float`类型：http://127.0.0.1:5000/project/10000
@app.route('/project/<float:item_str>')
def project(item_str):
    return 'project item is %s' % (item_str,)


# TODO: path类型
# TODO: http://127.0.0.1:5000/user/email/changeemail/123
# TODO: variable不能为空：http://127.0.0.1:5000/user/
@app.route('/user/<path:user_path>')
def userCenter(user_path):
    return 'user center url is %s' % (user_path,)


# import uuid
#
# print(uuid.uuid4())


# TODO: uuid类型
# TODO: http://127.0.0.1:5000/u/df78f232-f179-4351-97c8-ec4c8dc92542
@app.route('/u/<uuid:user_id>')
def user(user_id):
    return 'user id is %s' % (user_id,)


# TODO: any类型
# TODO: blog: http://127.0.0.1:5000/blog/123
# TODO: category: http://127.0.0.1:5000/category/123
@app.route('/<any(blog,category):url_path>/<int:id>')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情id：%s' % (id,)
    else:
        return '类目详情id：%s' % (id,)


# TODO: `search`传递参数模式
# TODO: http://127.0.0.1:5000/s?wd=python&ie=utf-8
@app.route('/s')
def search():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    return '你搜索的关键字wd：%s，ie: %s' % (wd, ie)


if __name__ == '__main__':
    app.run(debug=True)
