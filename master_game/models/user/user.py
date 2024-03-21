from master_game.models.character import CharacterSheet
import strawberry
from typing import List


@strawberry.type
class User:
    id: strawberry.ID
    username: str
    email: str
    age: int
    password: int
    avatar: str
    status: str
    sheets: List[CharacterSheet]
