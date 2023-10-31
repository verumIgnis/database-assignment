import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
conn.commit()
conn.close()