from flask import Blueprint, request,redirect, render_template, url_for, flash
from app import db
from app.models.user import User


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # Here you would typically set a session or token
            return redirect(url_for('auth.index'))
        else:
            flash('Invalid credentials', 'error')
            return render_template('login.html')
    return render_template('login.html')

@auth_bp.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return render_template('register.html')
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    # Here you would typically clear the session or token
    flash('You have been logged out', 'info')
    return redirect(url_for('auth.index'))
