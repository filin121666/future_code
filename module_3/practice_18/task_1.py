import sqlite3

conn = sqlite3.connect('my_db.db')
curr = conn.cursor()

firm = 'Samsung'
name = 'Galaxy S23'
price = '259'

curr.execute(f'INSERT INTO phones(firm, name, price) values("{firm}", "{name}", {price})')

firm = 'Samsung'
name = 'Galaxy S24 Ultra'
price = '499'

curr.execute(f'INSERT INTO phones(firm, name, price) values("{firm}", "{name}", {price})')

firm = 'Xiaomi'
name = 'Redmi Note 12 Pro'
price = '200'

curr.execute(f'INSERT INTO phones(firm, name, price) values("{firm}", "{name}", {price})')

firm = 'Xiaomi'
name = 'Redmi Poco M4 Pro'
price = '199'

curr.execute(f'INSERT INTO phones(firm, name, price) values("{firm}", "{name}", {price})')

firm = 'Xiaomi'
name = 'Redmi Note 12 S'
price = '150'

curr.execute(f'INSERT INTO phones(firm, name, price) values("{firm}", "{name}", {price})')

conn.commit()
conn.close()
