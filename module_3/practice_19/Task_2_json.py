from peewee import *
import hashlib
import json

db = SqliteDatabase('users.db')
db.connect()

psevdo_cookie = {"username": None}


class Users(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db


if len(Users.select()) > 0:
    psevdo_cookie['username'] = Users.select()[-1].username

psevdo_cookie = json.dumps(psevdo_cookie)


def reg(username, password):
    global psevdo_cookie
    if username != '' and username not in [us.username for us in Users.select()]:
        if password != '':
            Users.create(username=username, password=hashlib.sha256(
                password.encode('utf-8')).hexdigest())
            psevdo_cookie = json.loads(psevdo_cookie)
            psevdo_cookie.update({'username': Users.select()[-1].username})
            psevdo_cookie = json.dumps(psevdo_cookie)


def login(username, password):
    global psevdo_cookie
    for i in range(len(Users.select())):
        if username == Users.select()[i].username and hashlib.sha256(password.encode('utf-8')).hexdigest() == Users.select()[i].password:
            psevdo_cookie = json.loads(psevdo_cookie)
            psevdo_cookie.update({'username': username})
            psevdo_cookie = json.dumps(psevdo_cookie)
            return True
        else:
            return False


def corect(username, password, new_us, new_pass):
    global psevdo_cookie
    Users.update(username=new_us, password=hashlib.sha256(new_pass.encode('utf-8')).hexdigest()).where(Users.username == username and Users.password == hashlib.sha256(password.encode('utf-8')).hexdigest()).execute()
    psevdo_cookie = json.loads(psevdo_cookie)
    psevdo_cookie.update({'username': new_us})
    psevdo_cookie = json.dumps(psevdo_cookie)


with open('cookie.json', 'w') as file:
    file.truncate()
    # Здесь должны быть команды действий
    file.write(psevdo_cookie)

db.close()
