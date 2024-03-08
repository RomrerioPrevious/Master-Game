from graphene import ObjectType, ID, Int, String, List
from master_game.models.character import CharacterSheet


class User(ObjectType):
    id = ID
    username = String
    email = String
    age = Int
    password = Int
    avatar = String
    status = String
    sheets = List(CharacterSheet)
