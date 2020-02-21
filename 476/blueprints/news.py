from flask import Blueprint, render_template, url_for

news_app = Blueprint('news', __name__, url_prefix='/news')


@news_app.route('/list/')
def news_list():
    print(url_for('news.news_list'))
    return render_template('news/news_list.html')