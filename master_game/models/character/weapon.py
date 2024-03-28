from typing import TypedDict


class Weapon(TypedDict):
    id: int
    damage: int
    typeOfDamage: str
    distance: int
    weight: int
    counter: int
