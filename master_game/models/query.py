from ariadne import QueryType
from graphql import GraphQLResolveInfo
from .user import *
from .character import *
from master_game.services import UserService, CharacterService

query = QueryType()
user_service = UserService()
character_service = CharacterService()


@query.field("user")
def user(self, info: GraphQLResolveInfo, id: int) -> User:
    return user_service.get_user(id)


@query.field("charactersOfUser")
def characters_of_user(self, info: GraphQLResolveInfo, id: int) -> [CharacterSheet]:
    return user_service.get_user(id)["sheets"]


@query.field("character")
def character(self, info: GraphQLResolveInfo, id: int) -> CharacterSheet:
    return character_service.get_character(id)


@query.field("characterStats")
def character_stats(self, info: GraphQLResolveInfo, id: int) -> CharacterStats:
    return character_service.get_character(id)["stats"]


@query.field("armorOfCharacter")
def armor_of_character(self, info: GraphQLResolveInfo, id: int) -> [Armor]:
    return character_service.get_character(id)["armor"]


@query.field("armor")
def armor(self, info: GraphQLResolveInfo, id: int) -> Armor:
    ...


@query.field("weaponOfCharacter")
def weapon_of_character(self, info: GraphQLResolveInfo, id: int) -> [Weapon]:
    return character_service.get_character(id)["weapons"]


@query.field("weapon")
def weapon(self, info: GraphQLResolveInfo, id: int) -> Weapon:
    ...
