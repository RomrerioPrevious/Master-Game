from typing import TypedDict


class Armor(TypedDict):
    id: int
    armorClass: str
    hindranceToSecrecy: bool
    strengthRequirement: int
    weight: int
    counter: int
