from flask import Flask, render_template, url_for
from blueprints.news import news_app

app = Flask(__name__)
app.register_blueprint(news_app)


@app.route('/')
def index():
    print(url_for('news.news_list'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
