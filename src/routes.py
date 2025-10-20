from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

# Banco de dados em memória
users = []
next_id = 1

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users),200

@users_bp.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'Campos name e email são obrigatórios'}), 400

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
    for u in users:
        if u['id'] == user_id:
            return jsonify(u),200
    return jsonify({'error': 'Usuário não encontrado'}), 404


#atualizar
@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for u in users:
        if u['id'] == user_id:
            u['name'] = data.get('name', u['name'])
            u['email'] = data.get('email', u['email'])
            return jsonify({'message': 'Usuário atualizado com sucesso', 'user': u}), 200
    return jsonify({'error': 'Usuário não encontrado'}), 404

