from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'createtime': datetime(2020, 2, 12, 14, 53, 0)
    }
    return render_template('index.html', **context)


@app.template_filter('cuttime')
def handle_time(time):
    """
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2. 如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
    4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
    5. 否则就是显示具体的时间 2017/10/20 16:15
    """
    if isinstance(time, datetime):
        now = datetime.now()
        # TODO: 计算时间间隔包含了多少秒
        diff = (now - time).total_seconds()
        print(diff)
        if diff <= 60:
            return '刚刚'
        elif 60 < diff <= 60 * 60:
            return '%s分钟前' % int(diff / 60)
        elif 60 * 60 < diff <= 24 * 60 * 60:
            return '%s小时前' % int(diff / (60 * 60))
        elif 24 * 60 * 60 < diff <= 30 * 24 * 60 * 60:
            return '%s天前' % int(diff / (24 * 60 * 60))
        else:
            return time.strftime('%Y/%m/%d %H:%M:%S')
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True)
