from flask import Flask, render_template, Response, jsonify
# TODO: flask = werkzeug+sqlalchemy+jinja2
import uuid


class JSONResponse(Response):
    @classmethod
    def force_type(cls, response, environ):
        """
        非`Response`对象、非字符串、非元祖
        会调用`Response.force_type(rv,request.environ)`
        """
        if isinstance(response, dict):
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = JSONResponse


@app.route('/')
def hello_world():
    return render_template('index.html')


# TODO: 1.`Response`对象
@app.route('/list1/')
def list1():
    return Response('list1')


# TODO: 2.字符串
@app.route('/list2/')
def list2():
    res = Response('list2')
    res.set_cookie('web_lang', 'zh-cn')
    return res


# TODO: 3.元祖
@app.route('/list3/')
def list3():
    userid = uuid.uuid4()
    res = Response('list3', 200, {'webtoken': userid})
    return res


# TODO: 4.非`Response`对象、非字符串、非元祖
@app.route('/list4/', methods=['GET', 'POST'])
def list4():
    return {"username": "zhiliao", "age": 18}


if __name__ == '__main__':
    app.run(debug=True, host='192.168.31.176', port=8080)
