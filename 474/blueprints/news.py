from flask import Blueprint, render_template

news_app = Blueprint('news', __name__, url_prefix='/news', template_folder='views')

print(__name__)  # TODO: blueprints.news


@news_app.route('/all/')
def news_all():
    return render_template('news_all.html')
