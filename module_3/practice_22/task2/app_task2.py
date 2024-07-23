from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    res = 10 + 34
    return render_template('index.html', result=res)


app.run(host='0.0.0.0', port="5000")
