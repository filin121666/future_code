from flask import Flask
import requests

app2 = Flask("MyApp2")


@app2.route('/pong')
def pong():
    try:
        response = requests.get(url='http://127.0.0.1:5000/ping').text
        if response == 'ping':
            return 'pong'
        else:
            return response
    except:
        return 'waiting for a response'


if __name__ == '__main__':
    app2.run(host='0.0.0.0', port='5001')
