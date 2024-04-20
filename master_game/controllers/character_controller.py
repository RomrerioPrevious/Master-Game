from flask import Blueprint, request, jsonify
from master_game.services.character_service import CharacterService
from master_game.services.user_service import UserService
from master_game.models.character.character_sheet import CharacterSheet

app = Blueprint("character", __name__)


@app.route('/pers', methods=['POST'])
def create_character():
    user_id = int(request.cookies.get('user_id'))  # Получаем user_id из cookie
    user = UserService().get_user(user_id)
    character = CharacterSheet()
    CharacterService().add_character(character)
    UserService().update_user(user)


@app.route('/pers/<int:char_id>', methods=['PATCH'])
def update_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    user = UserService().get_user(user_id)
    character = CharacterService().get_character(char_id)
    if user["status"] == "admin":
        character.update_character(char_id)


@app.route('/pers/<int:char_id>', methods=['DELETE'])
def delete_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    user = UserService().get_user(user_id)
    if user["status"] == "admin":
        CharacterService().delete_character(char_id)


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    try:
        user = UserService().get_user(user_id)
        character = CharacterService().get_character(char_id)
    except Exception:
        return
    else:
        return character
