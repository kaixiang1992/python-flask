from flask import Blueprint, render_template

# TODO: 传递一个`subdomain`参数，来指定这个子域名的前缀
cms_app = Blueprint('cms', __name__, subdomain='cms')


@cms_app.route('/')
def cms_index():
    return render_template('cms/index.html')
