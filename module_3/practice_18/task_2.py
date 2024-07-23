import sqlite3
conn = sqlite3.connect('my_db.db')
curr = conn.cursor()

data = curr.execute('SELECT * FROM phones WHERE price<400').fetchall()
print(data)

conn.commit()
conn.close()
