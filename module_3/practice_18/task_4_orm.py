from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('my_db.db')


class phones(Model):
    firm = CharField()
    name = CharField()
    price = IntegerField()

    class Meta:
        database = db


db.connect()
phones.delete().where(phones.firm == 'Xiaomi').execute()
db.close()
