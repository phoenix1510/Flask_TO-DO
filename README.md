# Flask To-Do List

A simple multi-user To-Do List web application built with **Python and Flask**.  
This project was created as a learning project to understand Flask application structure, routing, authentication, forms, database operations, and CRUD functionality.

## Features

- User registration and login
- Secure password hashing
- Session-based authentication
- User-specific task management
- Add new tasks
- View all personal tasks
- Edit tasks
- Delete tasks
- Mark tasks as complete
- Task status management
- CSRF protection using Flask-WTF
- MySQL database integration
- Environment-based configuration
- Flask Blueprints for modular application structure

## Tech Stack

### Backend

- Python
- Flask
- Flask-WTF
- WTForms
- Werkzeug
- MySQL
- mysql-connector-python

### Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

### Database

MySQL is used to store users and tasks.

The database contains two main tables:

### `user`

| Column | Type | Description |
|---|---|---|
| `user_id` | INT | Primary key |
| `username` | VARCHAR(100) | Unique username |
| `password_hash` | VARCHAR(255) | Hashed password |

### `task`

| Column | Type | Description |
|---|---|---|
| `task_id` | INT | Primary key |
| `task_title` | VARCHAR(100) | Task title |
| `task_description` | MEDIUMTEXT | Task description |
| `user_id` | INT | Foreign key referencing `user` |
| `status` | ENUM | Task status |

Task statuses:

- `on_going`
- `complete`
- `discarded`

Each task belongs to a user through a foreign key relationship. Deleting a user also deletes their associated tasks through `ON DELETE CASCADE`.

## Project Structure

```text
Flask_TO-DO/
│
├── app/
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── db_operations.py
│   │   ├── init_db.py
│   │   └── schema.sql
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── main.py
│   │   └── wtfform.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   │
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── edit.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── welcome.html
│   │
│   └── __init__.py
│
├── .gitignore
├── README.md
└── run.py