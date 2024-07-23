from flask import render_template, Flask
from flask import request
import peewee

app = Flask(__name__)

db = peewee.SqliteDatabase('data.db')


class Users(peewee.Model):
    id = peewee.IntegerField(primary_key=True)
    username = peewee.CharField()

    class Meta:
        database = db


@app.route('/read_user')
def read_user():
    id = int(request.args.get('id'))
    if id:
        db.connect()
        result = Users.get(Users.id == id).username
        db.close()
        return render_template('read_user.html', res=result)
    else:
        return 'hello'


@app.route('/read_all_users')
def read_all_users():
    db.connect()
    result = Users.select()
    db.close()

    return render_template('read_all_users.html', res=result)

# не использовал автоинкремент в самой базе данных, потому что возникли сложности


@app.route('/create_user')
def create_user():
    username = request.args.get('username')
    if username:
        db.connect()
        res_id = Users.select()[-1].id + 1 if [i.id for i in Users.select().execute()] else 1
        Users.create(id=res_id, username=username)
        db.close()
        return render_template('confirm.html', res=res_id)
    else:
        return 'Введите значение username'


app.run(host='0.0.0.0', port=5000, debug=True)
