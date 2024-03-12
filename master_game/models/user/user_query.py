from master_game.models.character import CharacterSheet
from master_game.services import UserService
import strawberry
from typing import List


@strawberry.type
class UserQuery:
    @strawberry.field
    def id(self) -> strawberry.ID:
        ...

    @strawberry.field
    def username(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def age(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def password(self, id: strawberry.ID) -> int:
        ...

    @strawberry.field
    def email(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def avatar(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def status(self, id: strawberry.ID) -> str:
        ...

    @strawberry.field
    def sheets(self, id: strawberry.ID) -> List[CharacterSheet]:
        ...
