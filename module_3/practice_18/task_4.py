import sqlite3
conn = sqlite3.connect('my_db.db')
curr = conn.cursor()

curr.execute('DELETE FROM phones WHERE firm = "Xiaomi"')

conn.commit()
conn.close()
