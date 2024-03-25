from master_game.models.character import CharacterSheet
from typing import List, TypedDict


class User(TypedDict):
    id: int
    username: str
    email: str
    age: int
    password: int
    avatar: str
    status: str
    sheets: List[CharacterSheet]
