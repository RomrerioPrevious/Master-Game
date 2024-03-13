from typing import Any
from master_game.models.character import CharacterSheet
from master_game.models.user import User
from queue import Queue


class CacheService:
    _user = {}
    _user_delete_queue = Queue(1000)
    _character = {}
    _character_delete_queue = Queue(1000)

    def _get(self, id: int, get_dict: {int, Any}) -> Any:
        if id in get_dict.keys():
            return get_dict[id]
        return None

    def _add_or_update(self, id: int, update_object: Any, update_dict: {int, Any}, update_queue: Queue) -> None:
        if id not in update_dict.keys():
            if update_queue.full():
                self._delete_old(update_dict, update_queue)
            update_queue.put(id)
        update_dict[id] = update_object

    def _delete(self, id: int, update_dict: {int, Any}) -> None:
        if update_dict[id]:
            del update_dict[id]

    def _delete_old(self, delete_dict: {int, Any}, delete_queue: Queue) -> None:
        if not delete_queue.empty():
            id = delete_queue.get()
            if id in delete_dict.keys():
                del delete_dict[id]

    def get_user(self, id: int) -> User | None:
        return self._get(id, self._user)

    def add_or_update_user(self, id: int, user: User) -> None:
        self._add_or_update(id, user, self._user, self._user_delete_queue)

    def delete_user(self, id: int) -> None:
        self._delete(id, self._user)

    def delete_old_user(self) -> None:
        self._delete_old(self._user, self._user_delete_queue)

    def get_character(self, id: int) -> CharacterSheet | None:
        return self._get(id, self._user)

    def add_or_update_character(self, id: int, character: CharacterSheet) -> None:
        self._add_or_update(id, character, self._character, self._character_delete_queue)

    def delete_character(self, id: int) -> None:
        self._delete(id, self._character)

    def delete_old_character(self) -> None:
        self._delete_old(self._character, self._character_delete_queue)
