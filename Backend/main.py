from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import database

app = FastAPI()


# Registration model
class User(BaseModel):
    name: str
    email: str
    password: str


# Login model
class LoginUser(BaseModel):
    email: str
    password: str


# Home API
@app.get("/")
def home():
    return {
        "message": "Welcome to Interview Preparation Portal"
    }


# Register API
@app.post("/register")
def register_user(user: User):

    connection = sqlite3.connect("interview_portal.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (user.name, user.email, user.password)
    )

    connection.commit()
    connection.close()

    return {
        "message": "User registered successfully",
        "name": user.name,
        "email": user.email
    }


# Login API
@app.post("/login")
def login_user(user: LoginUser):

    connection = sqlite3.connect("interview_portal.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (user.email, user.password)
    )

    result = cursor.fetchone()

    connection.close()

    if result:
        return {
            "message": "Login successful",
            "name": result[1],
            "email": result[2]
        }

    return {
        "message": "Invalid email or password"
    }