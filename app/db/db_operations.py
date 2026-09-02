# all database operation will be performed in this file
from app.db.init_db import init_db
from app.db.init_db import close_db
from werkzeug.security import generate_password_hash

def get_user_from_username(username):
    db = init_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM user WHERE username = %s"
    cursor.execute(query,(username,))
    user = cursor.fetchone()
    cursor.close()
    close_db()
    return user

def insert_user(username, password):
    db = init_db()
    cursor = db.cursor()
    query = "INSERT INTO user(username, password) values(%s,%s)"
    password_hash = generate_password_hash(password)
    cursor.execute(query,(username,password_hash))
    db.commit()
    cursor.close()
    close_db()