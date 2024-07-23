import peewee
from flask import Flask, render_template, request, abort
import requests

app = Flask(__name__)

db = peewee.SqliteDatabase('users.db')


class Users(peewee.Model):
    id = peewee.AutoField(primary_key=True, unique=True)
    username = peewee.CharField(unique=True)
    password = peewee.CharField(unique=True)

    class Meta:
        database = db


@app.route('/form_create_user')
def form_create_user():
    return render_template('form_create_user.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')

    req = requests.post(url='http://127.0.0.1:5001/create_user_api',
                        json={'username': username, 'password': password})
    data: dict = req.json()

    if data.get('status_code') == 201:
        created_username = data.get('created_username')
        return render_template('info/create_user_info.html', res_username=created_username)
    elif data.get('status_code') == 400:
        abort(400)


@app.route('/read_all_users')
def read_all_users():
    data = requests.get(url='http://127.0.0.1:5001/read_all_users_api')
    result = data.json()
    return render_template('read_all_users.html', res=result)


@app.route('/form_update_user')
def form_update_user():
    return render_template('form_update_user.html')


@app.route('/update_user', methods=['POST'])
def update_user():
    old_username = request.form.get('old_username')
    old_password = request.form.get('old_password')
    new_username = request.form.get('new_username')
    new_password = request.form.get('new_password')
    req = requests.post(url='http://127.0.0.1:5001/update_user_api', json={'old_username': old_username,
                                                                           'old_password': old_password,
                                                                           'new_username': new_username,
                                                                           'new_password': new_password})
    data: dict = req.json()
    if data.get('status_code') == 200:
        updated_username = data.get('updated_username')
        return render_template('info/update_user_info.html', res_username=updated_username)
    elif data.get('status_code') == 404:
        abort(404)


@app.route('/form_delete_user')
def form_delete_user():
    return render_template('form_delete_user.html')


@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form.get('username')
    password = request.form.get('password')

    req = requests.post(url='http://127.0.0.1:5001/delete_user_api',
                        json={'username': username, 'password': password})
    data: dict = req.json()
    if data.get('status_code') == 200:
        return render_template('info/delete_user_info.html')
    elif data.get('status_code') == 404:
        abort(404)


@app.errorhandler(400)
def error_400(e):
    return render_template('errors/error_400.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('errors/error_404.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
