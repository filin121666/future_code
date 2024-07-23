from flask import Flask, request, jsonify, abort
import peewee


api = Flask(__name__)

db = peewee.SqliteDatabase('users.db')


class Users(peewee.Model):
    id = peewee.AutoField(primary_key=True, unique=True)
    username = peewee.CharField(unique=True)
    password = peewee.CharField(unique=True)

    class Meta:
        database = db


@api.route('/create_user_api', methods=['POST'])
def create_user_api():
    data: dict = request.json
    username = data.get('username')
    password = data.get('password')

    try:
        if username and password:
            db.connect()
            Users.create(username=username, password=password)
            db.close()
            return jsonify({'created_username': username, 'status_code': 201})
        else:
            abort(400)
    except:
        abort(400)


@api.route('/read_all_users_api')
def read_all_users_api():
    db.connect()
    result = [i.username for i in Users.select()]
    db.close
    return jsonify(result)


@api.route('/update_user_api', methods=['POST'])
def update_user_api():
    data: dict = request.json
    old_username = data.get('old_username')
    old_password = data.get('old_password')
    new_username = data.get('new_username')
    new_password = data.get('new_password')
    
    db.connect()
    user_info = list(Users.select().where(Users.username == old_username and Users.password == old_password))
    if user_info:
        Users.update(username=new_username, password=new_password).where(Users.username == old_username and Users.password == old_password).execute()
        db.close()
        return jsonify({'updated_username': new_username, 'status_code': 200})
    else:
        db.close()
        abort(404)
        

@api.route('/delete_user_api', methods=['POST'])
def delete_user_api():
    data: dict = request.json
    username = data.get('username')
    password = data.get('password')
    
    db.connect()
    user_info = list(Users.select().where(Users.username == username and Users.password == password))
    if user_info:
        Users.delete().where(Users.username == username and Users.password == password).execute()
        db.close()
        return jsonify({'status_code': 200})
    else:
        db.close()
        abort(404)


@api.errorhandler(400)
def error_400(e):
    return jsonify({'status_code': 400})


@api.errorhandler(404)
def error_404(e):
    return jsonify({'status_code': 404})


if __name__ == '__main__':
    api.run(host='127.0.0.1', port='5001', debug=True)
