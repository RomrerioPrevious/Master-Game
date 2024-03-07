import graphene
from master_game.models.character.armor import Armor
from master_game.models.character.stats import CharacterStats
from master_game.models.character.weapon import Weapon


class CharacterSheet(graphene.ObjectType):
    id = graphene.ID
    name: str
    classes: [str]
    rase: str
    maxHits: int
    hits: int
    stats: CharacterStats
    armorClass: int
    equipment: [str]
    weapons: [Weapon]
    armor: Armor
    skills: [str]
    featuresAndTraits: [str]
    skillBonus: int
    inspiration: int
    speed: int
    magic: [str]