import sqlite3

conn = sqlite3.connect("my_db.db")
curr = conn.cursor()

curr.execute('''CREATE TABLE "Users" (
	"id"	INTEGER UNIQUE,
	"username"	TEXT UNIQUE,
	"password"	TEXT UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);''')

conn.commit()
conn.close
