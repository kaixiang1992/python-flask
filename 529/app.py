from flask import Flask, request, g
from untils import log_a, log_b, log_c

app = Flask(__name__)


@app.route('/')
def hello_world():
    username = request.args.get('username')
    g.username = username
    log_a()
    log_b()
    log_c()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
