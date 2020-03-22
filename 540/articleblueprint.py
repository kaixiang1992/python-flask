from flask import Blueprint, render_template, make_response
from flask_restful import Api, fields, marshal_with, Resource
from models import Article

article_bp = Blueprint('article', __name__, url_prefix='/article')
# TODO: 1.在创建`Api`对象的时候，就不要再使用`app`了，而是使用蓝图
api = Api(article_bp)


# TODO: 2.使用`api.representation`这个装饰器来定义一个函数，在这个函数中，应该对`html`代码进行一个封装，再返回。
@api.representation(mediatype='text/html')
def output_html(data, code, headers):
    # print(data)  # TODO: html页面
    # print(code)  # TODO: 200
    # print(headers)  # TODO: {}

    # TODO: 在representation装饰的函数中，必须返回一个Response对象
    resp = make_response(data)
    return resp


# TODO: 标准化复杂参数示例 -- 根据文章返回信息
class ArtcicleView(Resource):
    resource_fileds = {
        "user_id": fields.Integer,
        "author": fields.Nested({  # TODO: 复杂结构 fields.Nested 返回字典
            "username": fields.String,
            "email": fields.String,
        }),
        "title": fields.String,
        "content": fields.String,
        "tags": fields.List(fields.Nested({  # TODO: 复杂结构 fields.List 返回列表
            "tag": fields.String
        })),
        "read_count": fields.Integer(default=80),  # TODO: 默认值
        "article_create_time": fields.String(attribute='create_time'),
        # todo: 重命名属性 create_time 以 article_create_time返回
    }

    @marshal_with(resource_fileds)
    def get(self, art_id):
        return Article.query.get(art_id)


# TODO: 标准化视图 -- 文章列表
class ListView(Resource):
    def get(self):
        return render_template('list.html')


api.add_resource(ArtcicleView, '/<art_id>/', endpoint='article')
api.add_resource(ListView, '/list/', endpoint='list')
