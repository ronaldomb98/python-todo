from flask import Flask
import sqlite3
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/")
def first_api():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return json.dumps(posts)