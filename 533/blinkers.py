from blinker import Namespace
from flask import request, g
from datetime import datetime

# TODO: 1.定义信号
mySignal = Namespace()
login_signal = mySignal.signal(name='login')


# TODO: 2.监听信号
# def loginForm(sender, username):
def loginForm(sender):
    # username = username
    username = g.username
    ip = request.remote_addr
    nowtime = datetime.now()
    login_log = '%s **** %s **** %s' % (username, ip, nowtime)
    print(login_log)
    with open('login_log.txt', 'a', encoding='utf-8') as fp:
        fp.write(login_log + '\n')


login_signal.connect(loginForm)
