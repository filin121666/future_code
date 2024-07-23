from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    # можно вводить (только, другие не желательно) примеры с умножением
    example = request.args.get('example')
    if example:
        res = eval(example)
        return render_template('index.html', res=res)

    res = 'not found'
    return render_template('index.html', res=res)


app.run(host='0.0.0.0', port='5000')
