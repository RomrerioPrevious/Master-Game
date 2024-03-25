from master_game.models.character.armor import Armor
from master_game.models.character.stats import CharacterStats
from master_game.models.character.weapon import Weapon
from typing import List, TypedDict


class CharacterSheet(TypedDict):
    id: int
    name: str
    classes: List[str]
    rase: str
    maxHits: int
    hits: int
    stats: CharacterStats
    armorClass: int
    equipment: List[str]
    weapons: List[Weapon]
    armor: Armor
    skills: List[str]
    featuresAndTraits: List[str]
    skillBonus: int
    inspiration: int
    speed: int
    magic: List[str]
