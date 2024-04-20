import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Reviews (
link TEXT NOT NULL,
review TEXT NOT NULL
)''')

conn.commit()
conn.close()
