from typing import Any
from queue import Queue


class CacheService:
    _model = {}
    _model_delete_queue = Queue(1000)

    def get(self, id: int) -> Any:
        if id in self._model.keys():
            return self._model[id]
        return None

    def add_or_update(self, id: int, update_object: Any) -> None:
        if id not in self._model.keys():
            if self._model_delete_queue.full():
                self.delete_old()
            self._model_delete_queue.put(id)
        self._model[id] = update_object

    def delete(self, id: int) -> None:
        if self._model[id]:
            del self._model[id]

    def delete_old(self) -> None:
        if not self._model_delete_queue.empty():
            id = self._model_delete_queue.get()
            if id in self._model.keys():
                del self._model[id]
