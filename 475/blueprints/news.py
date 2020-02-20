from flask import Blueprint, render_template

news_app = Blueprint('news', __name__, template_folder='views', static_folder='assets', url_prefix='/news')


@news_app.route('/list/')
def news_list():
    return render_template('news_list.html')


@news_app.route('/detail/')
def news_detail():
    return render_template('news_detail.html')