from flask import Flask, render_template, request, send_from_directory
# TODO: 使用werkzeug.utils.secure_filename来对上传上来的文件名进行一个过滤。
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
FILE_PATH = os.path.join(os.path.dirname(__file__), 'images')
print(FILE_PATH)    # TODO: D:\github\python-flask\512\images


@app.route('/')
def index():
    return render_template('index.html')


# TODO: 上传文件
@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        username = request.form.get('username')  # TODO: 用户昵称
        # TODO: 使用request.files.get('avatar')来获取文件
        avatar = request.files.get('avatar')
        # print(avatar)  # TODO: <FileStorage: '92dab2e31ea5f25eb77455cbceabff5.jpg' ('image/jpeg')>
        # print(type(avatar))  # TODO: <class 'werkzeug.datastructures.FileStorage'>
        # TODO: 处理文件名
        filename = secure_filename(avatar.filename)
        # TODO: 保存文件
        avatar.save(os.path.join(FILE_PATH, filename))

        return 'success'


# TODO: 查看文件
@app.route('/images/<filename>', methods=['GET'])
def getImage(filename):
    print(filename)
    # flask.send_from_directory(文件的目录,文件名)来获取文件
    return send_from_directory(FILE_PATH, filename)


if __name__ == '__main__':
    app.run(debug=True)
