from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase('my_db.db')
db.connect()


class phones(Model):
    firm = CharField()
    name = CharField()
    price = IntegerField()

    class Meta:
        database = db


phones.create_table()
phones.create(firm='Samsung', name='Galaxy S23', price='259')
phones.create(firm='Samsung', name='Galaxy S24 Ultra', price='499')
phones.create(firm='Xiaomi', name='Redmi Note 12 Pro', price='200')
phones.create(firm='Xiaomi', name='Redmi Poco M4 Pro', price='199')
phones.create(firm='Xiaomi', name='Redmi Note 12 S', price='150')

db.close()
