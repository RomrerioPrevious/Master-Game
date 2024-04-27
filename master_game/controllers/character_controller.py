from flask import Blueprint, request, redirect, url_for
from master_game.models.character.character_sheet import CharacterSheet
from master_game.models.character.weapon import Weapon
from master_game.models.character.armor import Armor
from master_game.models.character.stats import Stats
from master_game.services.character_service import CharacterService
import logging

logger = logging.getLogger("Logger")
logger.setLevel(logging.ERROR)
app = Blueprint("character", __name__)
characterService = CharacterService()


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


@app.route('/pers', methods=['POST'])
def create_character():
    try:
        character = inf()
        characterService.add_character(character)
        return redirect(url_for('character_page', char_id=character.id))
    except Exception as e:
        print(e)
        return False


@app.route('/pers/<int:charid>', methods=['PATCH'])
def update_character(char_id):
    try:
        character = inf()
        characterService.update_character(character)
        return redirect(url_for('character_page', charid=char_id))
    except Exception as e:
        print(e)
        return False


@app.route('/pers/<int:char_id>', methods=['DELETE'])
def delete_character(char_id):
    pass


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_character(char_id):
    pass


@app.route('/class', methods=['GET'])
def get_classes():  # Удалить?
    pass


@app.route('/species', methods=['GET'])
def get_species():  # Удалить?
    pass


@app.route('/random', methods=['GET'])
def get_random_character():  # Удалить?
    pass


@app.route('/random/cube', methods=['GET'])
def roll_cube():  # Удалить?
    pass


@app.route('/random/items', methods=['GET'])
def get_random_items():  # Удалить?
    pass
