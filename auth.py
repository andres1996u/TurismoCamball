from flask import Blueprint, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    if users_collection.find_one({'email': data['email']}):
        return jsonify({'error': 'El correo ya está registrado'}), 400

    hashed_password = generate_password_hash(data['password'])
    user = {
        'name': data['name'],
        'email': data['email'],
        'password': hashed_password,
        'created_at': datetime.utcnow()
    }
    users_collection.insert_one(user)
    return jsonify({'message': 'Usuario registrado con éxito'})

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users_collection.find_one({'email': data['email']})

    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'error': 'Correo o contraseña incorrectos'}), 401

    session['user_id'] = str(user['_id'])
    return jsonify({'message': 'Inicio de sesión exitoso'})

@auth.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Sesión cerrada con éxito'})
