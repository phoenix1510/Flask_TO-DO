# main dashboard blueprint for the application
from turtle import title
from app.routes.wtfform import addTaskForm, editTaskForm
from flask import Blueprint, render_template, session, redirect, url_for, flash,request
from app.db.db_operations import add_task_to_user, get_all_tasks, delete_task_from_user ,edit_task_of_user, mark_as_complete

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def welcome():
    return render_template('welcome.html')

@main_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Please log in to access the dashboard.', 'warning')
        return redirect(url_for('auth.login'))

    tasks = get_all_tasks(session['user_id'])

    add_form = addTaskForm()
    edit_form = editTaskForm()

    return render_template('dashboard.html',username=session['user'],tasks=tasks, add_form=add_form, edit_form=edit_form)

@main_bp.route('/dashboard/add_task', methods=['POST'])
def add_task():
    if 'user' not in session: 
        flash('Please log in to add tasks.', 'warning')
        return redirect(url_for('auth.login'))

    form = addTaskForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data

    if title and description:
        add_task_to_user(title, description, session['user_id'])
        flash('Task added successfully!', 'success')
    else:
        flash('Task title and description cannot be empty.', 'danger')
    return redirect(url_for('main.dashboard'))


@main_bp.route('/dashboard/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user' not in session:
        flash('Please log in to delete tasks.', 'warning')
        return redirect(url_for('auth.login'))
    
    delete_task_from_user(task_id, session['user_id'])
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('main.dashboard'))

@main_bp.route('/dashboard/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):

    if 'user' not in session:
        flash('Please log in to edit tasks.', 'warning')
        return redirect(url_for('auth.login'))

    form = editTaskForm()

    if form.validate_on_submit():

        title = form.title.data
        description = form.description.data

        edit_task_of_user(
            task_id,
            title,
            description,
            session['user_id']
        )

        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('edit.html', edit_form=form,task_id=task_id)

@main_bp.route('/dashboard/complete_task/<int:task_id>', methods=['GET','POST'])
def complete_task(task_id):
    if 'user' not in session:
        flash('Please log in to complete tasks.', 'warning')
        return redirect(url_for('auth.login'))

    mark_as_complete(task_id, session['user_id'])
    flash('Task marked as complete!', 'success')
    return redirect(url_for('main.dashboard'))