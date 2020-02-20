from flask import Flask, render_template
from blueprints.movie import movie_app
from blueprints.book import book_app

app = Flask(__name__)
# TODO: 注册`movie_app`蓝图
app.register_blueprint(movie_app)
# TODO: 注册`book_app`蓝图
app.register_blueprint(book_app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
