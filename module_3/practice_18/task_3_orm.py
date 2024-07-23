from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('my_db.db')


class phones(Model):
    firm = CharField()
    name = CharField()
    price = IntegerField()

    class Meta:
        database = db


db.connect()
phones.update(price=phones.price - 100).where(phones.firm == 'Samsung').execute()
db.close()
