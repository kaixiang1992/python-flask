from flask import Flask
import config
from db import db
from articleblueprint import article_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app=app)
app.register_blueprint(article_bp)


@app.route('/')
def index():
    return 'hello world!...'


if __name__ == '__main__':
    app.run(debug=True)
