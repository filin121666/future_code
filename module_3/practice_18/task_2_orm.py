from peewee import SqliteDatabase, Model, CharField, IntegerField
db = SqliteDatabase('my_db.db')


class phones(Model):
    firm = CharField()
    name = CharField()
    price = IntegerField()

    class Meta:
        database = db


db.connect()
result = phones.select().where(phones.price < 400)
my_list = [phone.name for phone in result]
print(my_list)
db.close()
