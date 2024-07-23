import sqlite3
conn = sqlite3.connect('my_db.db')
curr = conn.cursor()

curr.execute('UPDATE phones SET price = price - 100 WHERE firm="Samsung"')

conn.commit()
conn.close()
