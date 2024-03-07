from graphene import ObjectType, ID, Int


class CharacterStats(ObjectType):
    id = ID
    strength = Int
    dexterity = Int
    constitution = Int
    intelligence = Int
    wisdom = Int
    charisma = Int