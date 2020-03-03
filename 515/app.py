from flask import Flask, Response

app = Flask(__name__)


@app.route('/set/')
def setcookie():
    res = Response(response='设置cookie')
    res.set_cookie(key='username', value='zhiliao')
    return res


@app.route('/del/')
def delcookie():
    res = Response(response='删除cookie')
    res.delete_cookie(key='username')
    return res


if __name__ == '__main__':
    app.run(debug=True)
