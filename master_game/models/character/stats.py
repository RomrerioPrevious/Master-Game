import strawberry


@strawberry.type()
class CharacterStats:
    id: strawberry.ID
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
