from master_game.models.character.armor import Armor
from master_game.models.character.stats import CharacterStats
from master_game.models.character.weapon import Weapon
from typing import List
import strawberry


@strawberry.type
class CharacterSheetQuery:
    @strawberry.field
    def id(self) -> strawberry.ID:
        ...

    @strawberry.field
    def name(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def classes(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def rase(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def maxHits(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def hits(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def stats(self, id: strawberry.ID) -> CharacterStats:
        ...

    @strawberry.field
    def armorClass(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def equipment(self, id: strawberry.ID) -> List[str]:
        ...

    @strawberry.field
    def weapons(self, id: strawberry.ID) -> List[Weapon]:
        ...

    @strawberry.field
    def armor(self, id: strawberry.ID) -> Armor:
        ...

    @strawberry.field
    def skills(self, id: strawberry.ID) -> List[str]:
        ...

    @strawberry.field
    def featuresAndTraits(self, id: strawberry.ID) -> List[str]:
        ...

    @strawberry.field
    def skillBonus(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def inspiration(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def speed(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def magic(self, id: strawberry.ID) -> List[str]:
        ...
