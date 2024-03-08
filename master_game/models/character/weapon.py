from graphene import ObjectType, ID, Int, String


class Weapon(ObjectType):
    id = ID
    damage = String
    typeOfDamage = String
    distance = Int
    weight = Int
