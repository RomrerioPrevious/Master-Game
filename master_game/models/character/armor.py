import strawberry


@strawberry.type()
class Armor:
    id: strawberry.ID
    armorClass: str
    hindranceToSecrecy: bool
    strengthRequirement: int
    weight: int
