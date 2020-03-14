from flask import Flask
from werkzeug.local import Local
from threading import Thread

app = Flask(__name__)

local = Local()
local.request = '123'


class myThread(Thread):
    def run(self):
        local.request = 'abc'
        print('子线程：', local.request)


@app.route('/')
def hello_world():
    mythead = myThread()
    mythead.start()
    mythead.join()

    # print('主线程：', local.request)
    # print(local.request)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
