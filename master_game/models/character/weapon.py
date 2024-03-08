import strawberry


@strawberry.type()
class Weapon:
    id: strawberry.ID
    damage: str
    typeOfDamage: str
    distance: int
    weight: int
