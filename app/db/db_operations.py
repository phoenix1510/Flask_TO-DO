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

def add_task_to_user(title, description, user_id):
    db = init_db()
    cursor = db.cursor()
    query = "INSERT INTO task(task_title, task_description, user_id) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, description, user_id))
    db.commit()
    cursor.close()
    close_db()

def get_all_tasks(user_id):
    db = init_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM task WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    tasks = cursor.fetchall()
    cursor.close()
    close_db()
    return tasks

def delete_task_from_user(task_id, user_id):
    db = init_db()
    cursor = db.cursor()
    query = "DELETE FROM task WHERE task_id = %s AND user_id = %s"
    cursor.execute(query, (task_id, user_id))
    db.commit()
    cursor.close()
    close_db()

def edit_task_of_user(task_id, title, description, user_id):
    db = init_db()
    cursor = db.cursor()
    query = "UPDATE task SET task_title = %s, task_description = %s WHERE task_id = %s AND user_id = %s"
    cursor.execute(query, (title, description, task_id, user_id))
    db.commit()
    cursor.close()
    close_db()