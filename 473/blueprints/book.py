from flask import Blueprint

book_app = Blueprint('book', __name__, url_prefix='/book')


@book_app.route('/list/')
def book_list():
    return '图书列表'


@book_app.route('/detail')
def book_detail():
    return '图书详情'
