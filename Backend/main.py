from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Allow frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    name: str
    email: str
    password: str


@app.get("/")
def home():
    return {"message": "Welcome to Interview Preparation Portal"}


@app.post("/register")
def register_user(user: User):

    conn = sqlite3.connect("interview_portal.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT
        )
    """)

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (user.name, user.email, user.password)
    )

    conn.commit()
    conn.close()

    return {"message": "User registered successfully"}


@app.post("/login")
def login_user(user: User):

    conn = sqlite3.connect("interview_portal.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (user.email, user.password)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return {"message": "Login successful"}

    return {"message": "Invalid email or password"}
