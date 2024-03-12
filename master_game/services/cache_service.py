from master_game.models.user import User
from queue import Queue


class CacheService:
    _user = {}
    _user_delete_queue = Queue(1000)

    def get_user(self, id: int) -> User | None:
        if id in self._user.keys():
            return self._user[id]
        return None

    def add_or_update_user(self, id: int, user: User) -> None:
        if id not in self._user.keys():
            if self._user_delete_queue.full():
                self.delete_old_user()
            self._user_delete_queue.put(id)
        self._user[id] = user

    def delete_user(self, id: int) -> None:
        if self._user[id]:
            del self._user[id]

    def delete_old_user(self):
        if not self._user_delete_queue.empty():
            id = self._user_delete_queue.get()
            if id in self._user.keys():
                del self._user[id]
