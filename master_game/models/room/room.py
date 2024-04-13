from typing import TypedDict


class Room(TypedDict):
    id: int
    users: dict[int, {str: str}]
    characters: dict[
        str, {str: str | (int, int)}
    ]
    field: dict
