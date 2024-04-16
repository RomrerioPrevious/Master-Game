from typing import TypedDict


class Room(TypedDict):
    id: int
    users: dict[int, {str: str}]
    characters: dict[
        int, {str: str | (int, int)}
    ]
    field: dict
