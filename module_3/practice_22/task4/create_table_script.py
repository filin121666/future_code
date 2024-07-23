import sqlite3

conn = sqlite3.connect("data.db")
curr = conn.cursor()

curr.execute('''CREATE TABLE "users" (
	"id"	INTEGER,
	"username"	TEXT,
	PRIMARY KEY("id")
);''')

conn.commit()
conn.close
