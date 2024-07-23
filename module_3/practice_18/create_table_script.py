import sqlite3

conn = sqlite3.connect("my_db.db")
curr = conn.cursor()

curr.execute('''CREATE TABLE "phones" (
    "id"	INTEGER,
	"firm"	TEXT,
	"name"	TEXT,
	"price"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);''')

conn.commit()
conn.close
