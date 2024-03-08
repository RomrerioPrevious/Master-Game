import strawberry
from typing import List
from master_game.models.user import User
from master_game.models.character import CharacterSheet


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: strawberry.ID) -> User:
        ...

    @strawberry.field
    def character(self, id: strawberry.ID) -> CharacterSheet:
        ...

    @strawberry.field
    def character_stats(self, id_of_character: strawberry.ID) -> CharacterSheet:
        ...

    @strawberry.field
    def character_equipment(self, id_of_character: strawberry.ID) -> CharacterSheet:
        ...

    @strawberry.field
    def character_fight_equipment(self, id_of_character: strawberry.ID) -> CharacterSheet:
        ...