from ariadne import QueryType
from .user import *
from .character import *

query = QueryType()


@query.field("user")
def user(self, info, id: int) -> User:
    ...


@query.field("charactersOfUser")
def characters_of_user(self, info, id: int) -> [CharacterSheet]:
    ...


@query.field("character")
def character(self, info, id: int) -> CharacterSheet:
    ...


@query.field("characterStats")
def character_stats(self, info, id: int) -> CharacterStats:
    ...


@query.field("armorOfCharacter")
def armor_of_character(self, info, id: int) -> [Armor]:
    ...


@query.field("armor")
def armor(self, info, id: int) -> Armor:
    ...


@query.field("weaponOfCharacter")
def weapon_of_character(self, info, id: int) -> [Weapon]:
    ...


@query.field("weapon")
def weapon(self, info, id: int) -> Weapon:
    ...
