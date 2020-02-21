from flask import Flask, render_template
from blueprint.cms import cms_app

app = Flask(__name__)
# TODO: 指定域名
app.config['SERVER_NAME'] = 'womai.com:5000'
app.register_blueprint(cms_app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
