from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import database

app=FastAPI()

class User(BaseModel):
    name:str
    email:str
    password:str

@app.get("/")
def home():
    return{'message':'Welcome to Interview Preparation Portal'}

@app.post('/register')
def register_user(user: User):

    connection=sqlite3.connect('interview_portal.db')
    cursor=connection.cursor()

    cursor.execute(
        'INSERT INTO users(name, email, password) VALUES (?, ?, ?)',
        (user.name, user.email, user.password)
    )
    connection.commit()
    connection.close()

    return {
        'message':'User registered successfully',
    'name':user.name,
    'email':user.email
    }
