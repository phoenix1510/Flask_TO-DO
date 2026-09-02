# main dashboard blueprint for the application
from flask import Blueprint, render_template, session, redirect, url_for, flash,request
from app.db.db_operations import add_task_to_user, get_all_tasks, delete_task_from_user ,edit_task_of_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def welcome():
    return render_template('welcome.html')

@main_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', username=session['user'])

@main_bp.route('/dashboard/add_task', methods=['POST'])
def add_task():
    if 'user' not in session: 
        flash('Please log in to add tasks.', 'warning')
        return redirect(url_for('auth.login'))

    task = request.form.get('task')        #json sent by js

    if task: 
        add_task_to_user(task['title'], task['description'], session['user_id'])
        flash('Task added successfully!', 'success')
    else:
        flash('Task title and description cannot be empty.', 'danger')
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard/get_tasks', methods=['GET'])
def get_tasks():
    if 'user' not in session:
        flash('Please log in to view tasks.', 'warning')
        return redirect(url_for('auth.login'))
    tasks = get_all_tasks(session['user_id'])
    return render_template('tasks.html', tasks=tasks)

@main_bp.route('/dashboard/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user' not in session:
        flash('Please log in to delete tasks.', 'warning')
        return redirect(url_for('auth.login'))
    
    delete_task_from_user(task_id, session['user_id'])
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard/edit_task', methods=['POST'])
def edit_task():
    if 'user' not in session: 
        flash('Please log in to edit tasks.', 'warning')
        return redirect(url_for('auth.login'))

    title= request.form.get('title')
    description = request.form.get('description')
    task_id =request.form.get('task_id')

    if task_id and title and description:
        edit_task_of_user(task_id, title, description, session['user_id'])
        flash('Task updated successfully!', 'success')
    else:
        flash('Task title and description cannot be empty.', 'danger')
    return redirect(url_for('main.dashboard'))