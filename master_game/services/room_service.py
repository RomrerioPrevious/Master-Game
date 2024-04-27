from master_game.models import User
from master_game.models.room import Room
from master_game.services.cache_service import CacheService
from master_game.config import ROOMS_PATH
import json


class RoomService:
    def __init__(self):
        self.json_path = ROOMS_PATH
        self.active_rooms_ids = set()
        with open(self.json_path, "r", encoding="UTF-8") as file:
            self.data: dict = json.load(file)

    def create_room(self, id: int, user: int) -> None:
        room = Room(id=id,
                    users={user: {"status": "master"}},
                    characters={},
                    field={"scale": (15, 15)})
        self.active_rooms_ids.add(id)
        self.data[id] = room

    def get_room(self, id: int) -> Room:
        room = self.data[id]
        return room

    def get_active_ids(self) -> set:
        return self.active_rooms_ids

    def close_room(self, id: int) -> None:
        del self.data[id]
        self.active_rooms_ids.remove(id)
