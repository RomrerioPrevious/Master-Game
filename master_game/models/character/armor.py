from graphene import ObjectType, ID, Int, String, Boolean


class Armor(ObjectType):
    id = ID
    armorClass = String
    hindranceToSecrecy = Boolean
    strengthRequirement = Int
    weight = Int
