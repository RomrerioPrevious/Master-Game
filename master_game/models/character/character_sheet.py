from graphene import ObjectType, ID, Int, String, List
from master_game.models.character.armor import Armor
from master_game.models.character.stats import CharacterStats
from master_game.models.character.weapon import Weapon


class CharacterSheet(ObjectType):
    id = ID
    name = String
    classes = List(String)
    rase = String
    maxHits = Int
    hits = Int
    stats = CharacterStats
    armorClass = Int
    equipment = List(String)
    weapons = [Weapon]
    armor = Armor
    skills = List(String)
    featuresAndTraits = List(String)
    skillBonus = Int
    inspiration = Int
    speed = Int
    magic = List(String)
