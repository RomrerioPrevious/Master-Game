import strawberry


@strawberry.type
class CharacterStats:
    id: strawberry.ID
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


@strawberry.type
class CharacterStatsQuery:
    @strawberry.field
    def id(self) -> strawberry.ID:
        ...

    @strawberry.field
    def strength(self) -> int:
        ...

    @strawberry.field
    def dexterity(self) -> int:
        ...

    @strawberry.field
    def constitution(self) -> int:
        ...

    @strawberry.field
    def intelligence(self) -> int:
        ...

    @strawberry.field
    def wisdom(self) -> int:
        ...

    @strawberry.field
    def charisma(self) -> int:
        ...