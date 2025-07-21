from flask import Blueprint, request,redirect, render_template, jsonify
from app import db
from app.models.user import User


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            # Here you would typically create a session or token for the user
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401

    return render_template('login.html')
    
@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"message": "User already exists"}), 409
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully"}), 201

    return render_template('register.html')
    