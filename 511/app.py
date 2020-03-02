from flask import Flask, render_template, request
from validators import SettingForm

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        context = {
            'form': SettingForm()
        }
        return render_template('settings.html', **context)
    else:
        form = SettingForm(request.form)
        print(form.errors)
        return 'success...'


if __name__ == '__main__':
    app.run(debug=True)
