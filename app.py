from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect('/home/vagrant/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/')
def read_root():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return {'items': [dict(item) for item in items]}