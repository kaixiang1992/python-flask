from flask import Flask, Response
from datetime import datetime, timedelta


app = Flask(__name__)


@app.route('/')
def index():
    res = Response(response='设置cookie失效时间')
    # TODO: 1.max_age：以秒为单位，距离现在多少秒后cookie会过期
    # res.set_cookie(key='username', value='zhiliao', max_age=60)
    # TODO: 2.expires：为`datetime类型`。这个时间需要设置为格林尼治时间，也就是要距离北京少8个小时的时间
    expirestime = datetime.now() + timedelta(days=1)
    print(expirestime)
    res.set_cookie(key='username', value='zhiliao', expires=expirestime)
    return res


if __name__ == '__main__':
    app.run(debug=True)
