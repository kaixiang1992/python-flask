from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        "script": "<script>console.log(123);</script>",
        # "escapestr": "%3Ch1%3Ee转义的h1标签%3C%2Fh1%3E",
        "escapestr": "<h5>转义的h5标签</h5>",
        "persons": ["zhiliao", "ketang"],
        "age": "18",
        "replacestr": "hello aaa, hello bbb, hello ccc",
        "longtxt": "2月10日下午，习近平来到北京地坛医院。在地坛医院办公楼远程诊疗中心，习近平通过视频连线武汉市收治新冠肺炎患者的金银潭医院、协和医院、火神山医院，向疫情防控一线的医务工作者、干部职工和人民解放军指战员了解情况、听取意见和建议。",

    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
