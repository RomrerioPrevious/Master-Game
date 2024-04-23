from master_game.models.character.character_sheet import CharacterSheet
from master_game.services.character_service import CharacterService
from master_game.services.user_service import UserService
from master_game.config import Logger
from flask import Blueprint, request

app = Blueprint("character", __name__)

character_service = CharacterService()
user_service = UserService()


@app.route("/pers/<int:char_id>", methods=["GET"])
def get_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    try:
        user = user_service.get_user_by_id(user_id)
        character = character_service.get_character(char_id)
        if character not in user["sheets"]:
            raise Exception(f"Not found character with id={char_id}")
        return character
    except Exception as ex:
        Logger.write_error(ex)


@app.route("/pers", methods=["POST"])
def create_character():
    user_id = int(request.cookies.get("user_id"))
    user = user_service.get_user_by_id(user_id)
    character = CharacterSheet()
    character_service.add_character(character)
    user["sheets"].append(character)
    UserService().update_user(user)


@app.route("/pers/<int:char_id>", methods=["PATCH"])
def update_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    user = user_service.get_user_by_id(user_id)
    character = character_service.get_character(char_id)
    if user["status"] == "admin" or character in user["sheets"]:
        character.update_character(char_id)


@app.route("/pers/<int:char_id>", methods=["DELETE"])
def delete_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    user = UserService().get_user_by_id(user_id)
    character = character_service.get_character(char_id)
    if user["status"] == "admin" or character in user["sheets"]:
        character_service.delete_character(char_id)
        user["sheets"].remove(character)
    user_service.update_user(user)
