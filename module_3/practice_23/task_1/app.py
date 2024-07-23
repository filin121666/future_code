import peewee

from flask import Flask, render_template, request


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

    db.connect()
    Users.create(username=username, password=password)
    db.close()

    return render_template('create_info.html', res_username=username)


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
        return render_template('update_info.html', res_username=new_username, res_password=new_password)
    else:
        db.close()
        return '<h2>Ошибка! Возможно такого пользователя не существует или данные введены не верно.</h2>'


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
        return render_template('delete_info.html')
    else:
        db.close()
        return '<h2>Ошибка! Возможно такого пользователя не существует или данные введены не верно.</h2>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
