import strawberry


@strawberry.type
class Armor:
    id: strawberry.ID
    armorClass: str
    hindranceToSecrecy: bool
    strengthRequirement: int
    weight: int


@strawberry.type
class ArmorQuery:
    @strawberry.field
    def id(self) -> strawberry.ID:
        ...

    @strawberry.field
    def armorClass(self) -> str:
        ...

    @strawberry.field
    def hindranceToSecrecy(self) -> bool:
        ...

    @strawberry.field
    def strengthRequirement(self) -> int:
        ...

    @strawberry.field
    def weigh(self) -> int:
        ...
