import peewee
from flask import Flask, render_template, request, jsonify, abort

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

    if username and password:
        db.connect()
        Users.create(username=username, password=password)
        db.close()
        return jsonify({'created_user': username})
    else:
        abort(400)


@app.route('/read_all_users')
def read_all_users():
    db.connect()
    result = Users.select()
    db.close

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

    db.connect()
    user_info = list(Users.select().where(Users.username == old_username and Users.password == old_password))
    if user_info:
        Users.update(username=new_username, password=new_password).where(
            Users.username == old_username and Users.password == old_password).execute()
        db.close()
        return jsonify({'updated_username': new_username, 'updated_password': new_password})
    else:
        db.close()
        abort(404)


@app.route('/form_delete_user')
def form_delete_user():
    return render_template('form_delete_user.html')


@app.route('/delete_user', methods=['POST'])
def delete_user():
    username = request.form.get('username')
    password = request.form.get('password')

    db.connect()
    user_info = list(Users.select().where(Users.username == username and Users.password == password))
    if user_info:
        Users.delete().where(Users.username == username and Users.password == password).execute()
        db.close()
        return jsonify({'deleted_user': username})
    else:
        db.close()
        abort(404)


@app.errorhandler(400)
def error_400(e):
    return render_template('errors/error_400.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('errors/error_404.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
