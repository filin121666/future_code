from peewee import *
import hashlib

db = SqliteDatabase('users.db')
db.connect()


class Users(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db


def reg(username, password):
    if username != '' and username not in [us.username for us in Users.select()]:
        if password != '':
            Users.create(username=username, password=hashlib.sha256(
                password.encode('utf-8')).hexdigest())


def login(username, password):
    for i in range(len(Users.select())):
        if username == Users.select()[i].username and hashlib.sha256(password.encode('utf-8')).hexdigest() == Users.select()[i].password:
            return True
        else:
            return False


def corect(username, password, new_us, new_pass):
    Users.update(username=new_us, password=hashlib.sha256(new_pass.encode('utf-8')).hexdigest()).where(Users.username == username and Users.password == hashlib.sha256(password.encode('utf-8')).hexdigest()).execute()

# Здесь должны быть команды


db.close()
