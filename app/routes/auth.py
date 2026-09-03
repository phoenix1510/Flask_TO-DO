# auth blueprint for login and registration routes

from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.db.db_operations import get_user_from_username, insert_user
from app.routes.wtfform import LoginForm, SignupForm

auth_bp = Blueprint('auth',__name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = get_user_from_username(username)
        if user and check_password_hash(user['password_hash'], password):
            flash('Login successful!', 'success')
            session['user'] = user['username']
            session['user_id'] = user['user_id']
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', None)
        flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        existing_user = get_user_from_username(username)
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            insert_user(username, password)
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)