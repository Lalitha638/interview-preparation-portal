import sqlite3


def create_table():

    conn = sqlite3.connect("interview_portal.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_user(name, email, password):

    conn = sqlite3.connect("interview_portal.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    """, (name, email, password))

    conn.commit()
    conn.close()