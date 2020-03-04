from flask import Blueprint, request

cms = Blueprint('cms', __name__, subdomain='cms')


@cms.route('/')
def cmshome():
    username = request.cookies.get('username')
    if username:
        return 'cms.testflask.com:5000读取的cookie信息为：%s' % username
    else:
        return 'cms.testflask.com:5000没有读取的到任何cookie信息'