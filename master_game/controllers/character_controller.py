from flask import Blueprint, request, jsonify
import sqlite3

app = Blueprint("character", __name__)


@app.route('/pers', methods=['POST'])
def create_character():
    pass


@app.route('/pers/<int:char_id>', methods=['PATCH'])
def update_character(char_id):
    pass


@app.route('/pers/<int:char_id>', methods=['DELETE'])
def delete_character(char_id):
    pass


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_character(char_id):
    pass


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_characters_weapon_id(char_id):
    name, damage, typeOfDamage, distance, weight = "sword", 10, "bless", 6, 3
    id = '0'
    hashedName = hashing_string(name, 4, 3, -2)
    hashedTOD = hashing_string(typeOfDamage, 4, 3, -2)
    id += hashedName + hashedTOD
    id += str(distance % 10)
    id = max(-2147483648, min(int(id) + (damage * weight) // 2, 2147483647))
    return id


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_characters_armor_id(char_id):
    name, armorClass, hindranceToSecrecy, strengthRequirement, weight = "leatherVest", "lats", True, 6, 3
    id = str(int(hindranceToSecrecy))
    hashedName = hashing_string(name, 6, 4, -2)
    hashedAC = hashing_string(armorClass, 3, 3, -1)
    id += hashedName.ljust(6, '0') + hashedAC.ljust(3, '0')
    id = max(-2147483648, min(int(id) + (strengthRequirement + weight) // 2, 2147483647))
    return id


def hashing_string(string, needLenght, step, stepForLenght):
    hashed, zagotovka = '', ''
    for code in map(lambda x: str(ord(x)), string):
        zagotovka += code
    for i in range(1, len(zagotovka), step):
        hashed += str((int(zagotovka[i]) + int(zagotovka[i - 1])) % 10)
    while len(hashed) > needLenght:
        hashed = str(int(hashed[:stepForLenght]) + int(hashed[stepForLenght:]))
    return hashed.ljust(needLenght, '0')


print(get_characters_weapon_id(-0))
print(get_characters_armor_id(-0))


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
