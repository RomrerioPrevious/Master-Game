from master_game.models.character import CharacterSheet
from typing import List, TypedDict


class User(TypedDict):
    id: int
    username: str
    email: str
    age: int
    password: int
    status: str
    sheets: List[CharacterSheet]

"""
    id: int = Column(Integer,
                     primary_key=True, autoincrement=True)
    username: str = Column(String)
    email: str = Column(String)
    age: int = Column(Integer)
    password: int = Column(Integer)
    status: str = Column(String)
    sheets: List[CharacterSheet] = Column(ARRAY,
                                          ForeignKey("characters.id"))
                                          """