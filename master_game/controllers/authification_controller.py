import random
from flask import Blueprint, request, jsonify

app = Blueprint("auth", __name__)


@app.route('/auth', methods=['GET'])
def auth():
    # TODO: authentication
    return jsonify({'message': 'Authentication successful'})


@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.json
    new_user_id = random.randint(10000, 99999)
    # TODO: creation account
    return jsonify({'message': f"User created successfully. User's id: {new_user_id}"})


@app.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user_data = request.json
    # TODO: update users
    return jsonify({'message': 'User updated successfully'})


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # TODO: delete users
    return jsonify({'message': 'User deleted successfully'})


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # TODO: get users
    return jsonify({'user_id': user_id, 'name': 'Test User'})
