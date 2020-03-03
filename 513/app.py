from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
# TODO: CombinedMultiDict 来把`request.form`与`request.files`来进行合并
from werkzeug.datastructures import CombinedMultiDict
from validators import UploadForm
import os

app = Flask(__name__)
FILE_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # TODO: CombinedMultiDict([ImmutableMultiDict([('username', '')]), ImmutableMultiDict([('avatar',
        #  <FileStorage: '0.gif' ('image/gif')>)])])
        # print(CombinedMultiDict(dicts=[request.form, request.files]))
        # TODO: <class 'werkzeug.datastructures.CombinedMultiDict'>
        # print(type(CombinedMultiDict(dicts=[request.form, request.files])))
        form = UploadForm(CombinedMultiDict(dicts=[request.form, request.files]))
        if form.validate():
            # TODO: 获取方式一
            # username = request.form.get('username')
            # avatar = request.files.get('avatar')
            # TODO: 获取方式二
            username = form.username.data
            avatar = form.avatar.data
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(FILE_PATH, filename))
            return '文件上传成功'
        else:
            print(form.errors)
            return 'fail'


@app.route('/images/<filename>', methods=['GET'])
def getImage(filename):
    return send_from_directory(FILE_PATH, filename)


if __name__ == '__main__':
    app.run(debug=True)
