import sqlite3
connection=sqlite3.connect('interview_portal.db')
cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT NOT NULL,
password TEXT NOT NULL
)
""")

connection.commit()
connection.close()
