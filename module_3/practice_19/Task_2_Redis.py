from peewee import *
import hashlib
import redis

rdb = redis.Redis(host='localhost', port=6379, decode_responses=True)
rdb.set('username', 'None')

db = SqliteDatabase('users.db')
db.connect()


class Users(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db


if len(Users.select()) > 0:
    rdb.set('username', Users.select()[-1].username)


def reg(username, password):
    if username != '' and username not in [us.username for us in Users.select()]:
        if password != '':
            Users.create(username=username, password=hashlib.sha256(
                password.encode('utf-8')).hexdigest())
            rdb.set('username', Users.select()[-1].username)


def login(username, password):
    for i in range(len(Users.select())):
        if username == Users.select()[i].username and hashlib.sha256(password.encode('utf-8')).hexdigest() == Users.select()[i].password:
            rdb.set('username', username)
            return True
        else:
            return False


def corect(username, password, new_us, new_pass):
    Users.update(username=new_us, password=hashlib.sha256(new_pass.encode('utf-8')).hexdigest()).where(Users.username == username and Users.password == hashlib.sha256(password.encode('utf-8')).hexdigest()).execute()
    rdb.set('username', new_us)

# Здесь должны быть команды


db.close()
