from flask import Flask

app1 = Flask("MyApp1")


@app1.route('/ping')
def ping():
    return 'ping'


if __name__ == '__main__':
    app1.run(host='0.0.0.0', port='5000')
