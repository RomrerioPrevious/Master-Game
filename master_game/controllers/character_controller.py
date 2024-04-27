from master_game.services.character_service import CharacterService
from master_game.services.user_service import UserService
from master_game.models.character.character_sheet import CharacterSheet
from master_game.config import Logger
from flask import Blueprint, request, redirect, url_for
from master_game.models.character.weapon import Weapon
from master_game.models.character.armor import Armor
from master_game.models.character.stats import Stats
import logging

app = Blueprint("character", __name__)
character_service = CharacterService()
user_service = UserService()
logger = logging.getLogger("Logger")
logger.setLevel(logging.ERROR)


def inf():
    data = request.form
    armor = Armor(id=data["id"], name=data["name"], armorClass=data["armorClass"],
                  hindranceToSecrecy=data["hindranceToSecrecy"], strengthRequirement=data["strengthRequirement"],
                  weight=data["weight"], counter=data["counter"])
    weapon = Weapon(id=data["id"], name=data["name"], damage=data["damage"], typeOfDamage=data["typeOfDamage"],
                    distance=data["distance"], weight=data["weight"], counter=data["counter"])
    stats = Stats(id=data["id"], strength=data["strength"], dexterity=data["dexterity"],
                  constitution=data["constitution"], intelligence=data["intelligence"], wisdom=data["wisdom"],
                  charisma=data["charisma"])
    character = CharacterSheet(id=data["id"], name=data['name'], classes=data["classes"],
                               rase=data['rase'], maxHits=data['maxHits'], hits=data['hits'], stats=stats,
                               armorClass=data['armorClass'], equipment=data['equipment'], weapons=weapon,
                               armor=armor, skills=data['skills'],
                               featuresAndTraits=data["featuresAndTraits"], skillBonus=data['skillBonus'],
                               inspiration=data['inspiration'], speed=data['speed'], magic=data['magic'])
    return character


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


@app.route('/pers', methods=['POST'])
def create_character():
    try:
        character = inf()
        character_service.add_character(character)
        return redirect(url_for('character_page', char_id=character.id))
    except Exception as e:
        print(e)
        return False


@app.route('/pers/<int:charid>', methods=['PATCH'])
def update_character(char_id):
    try:
        character = inf()
        character_service.update_character(character)
        return redirect(url_for('character_page', charid=char_id))
    except Exception as e:
        print(e)
        return False


@app.route('/pers/<int:char_id>', methods=['DELETE'])
@app.route("/pers/<int:char_id>", methods=["DELETE"])
def delete_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    user = UserService().get_user(user_id)
    character = CharacterService().get_character(char_id)
    user = UserService().get_user_by_id(user_id)
    character = character_service.get_character(char_id)
    if user["status"] == "admin" or character in user["sheets"]:
        CharacterService().delete_character(char_id)
        character_service.delete_character(char_id)
        user["sheets"].remove(character)
    UserService().update_user(user)


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_character(char_id):
    user_id = int(request.cookies.get("user_id"))
    try:
        user = UserService().get_user(user_id)
        character = CharacterService().get_character(char_id)
        if character not in user["sheets"]:
            raise Exception(f"Not found character with id={char_id}")
    except Exception:
        return
    return character
    user_service.update_user(user)
