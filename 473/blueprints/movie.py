from flask import Blueprint

movie_app = Blueprint('movie', __name__, url_prefix="/movie")


@movie_app.route('/list/')
def movie_list():
    return '电影列表'


@movie_app.route('/detail/')
def movie_detail():
    return '电影详情'
