from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

# Banco de dados em memória
users = []
next_id = 1

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@users_bp.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    user = {
        'id': next_id,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users.append(user)
    next_id += 1
    return jsonify(user), 201

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return jsonify({'error': 'Usuário não encontrado'}), 404
