from flask import Blueprint, request, jsonify
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Here you would typically check the username and password against your database
    # For simplicity, we will just return a success message
    if username and password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 400 
    
@auth_bp.route('/register', methods=['POST'])
def register(): 
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Here you would typically save the user to your database
    # For simplicity, we will just return a success message
    if username and password:
        return jsonify({"message": "Registration successful"}), 201
    else:
        return jsonify({"message": "Invalid input"}), 400
    