from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'users': ['zhiliao1', 'zhiliao2', 'zhiliao3'],
        'person': {
            'username': 'zhiliao',
            'age': 18,
            'country': 'china'
        },
        'books': [
            {
                'bookname': '三国演义',
                'author': '罗贯中',
                'price': 110
            },
            {
                'bookname': '西游记',
                'author': '吴承恩',
                'price': 100
            },
            {
                'bookname': '水浒传',
                'author': '施耐庵',
                'price': 120
            },
            {
                'bookname': '红楼梦',
                'author': '曹雪芹',
                'price': 120
            }
        ]
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
