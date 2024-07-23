from flask import Flask

app = Flask(__name__)

@app.route('/hello_docker')
def hello_docker():
    return 'Hello, Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')