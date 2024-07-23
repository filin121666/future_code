import requests
import json
from flask import Flask, jsonify

app = Flask('currency')

@app.route('/currency_valute')
def get_currency():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    data = response['Valute']['USD']['Value']
    return jsonify(data)

app.run(host='127.0.0.1', port='5000')