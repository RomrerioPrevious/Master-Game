import strawberry


@strawberry.type
class Weapon:
    id: strawberry.ID
    damage: str
    typeOfDamage: str
    distance: int
    weight: int


@strawberry.type
class WeaponQuery:
    @strawberry.field
    def id(self) -> strawberry.ID:
        ...

    @strawberry.field
    def damage(self) -> str:
        ...

    @strawberry.field
    def typeOfDamage(self) -> str:
        ...

    @strawberry.field
    def distance(self) -> int:
        ...

    @strawberry.field
    def weight(self) -> int:
        ...