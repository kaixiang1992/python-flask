from flask import Flask
from flask_restful import Api, Resource, fields, marshal_with
import config
from db import db
from models import User, Article, Tags

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)
api = Api(app)

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


api.add_resource(ArtcicleView, '/article/<art_id>/', endpoint='article')


# TODO: 标准化复杂参数示例 -- 根据标签返回信息
class TagView(Resource):
    resource_fileds = {
        'id': fields.Integer,
        'tag': fields.String,
        'articles': fields.List(fields.Nested({
            'artcicle_id': fields.Integer
        })),
        'create_time': fields.String
    }

    @marshal_with(resource_fileds)
    def get(self, tag_id):
        return Tags.query.get(tag_id)


api.add_resource(TagView, '/tag/<tag_id>/', endpoint='tag')


@app.route('/')
def index():
    # user1 = User(username='zhiliao', email='zhiliao@163.com')
    # user2 = User(username='ketang', email='ketang@163.com')
    # article1 = Article(title='python大法好', content='flask、django真好')
    # article2 = Article(title='Javascript大法好', content='vue MVVM')
    # tag1 = Tags(tag='IT')
    # tag2 = Tags(tag='Python')
    # tag3 = Tags(tag='Javascript')
    # article1.author = user1
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    # article2.author = user2
    # article2.tags.append(tag1)
    # article2.tags.append(tag3)
    # TODO: 提交数据
    # db.session.add_all([article1, article2])
    # db.session.commit()
    return 'hello world!...'


if __name__ == '__main__':
    app.run(debug=True)
