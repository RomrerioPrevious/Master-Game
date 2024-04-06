from master_game.services.cache_service import CacheService


class CharacterService:
    def __init__(self):
        self._cash_service = CacheService()

    def get_character(self, id: int) -> dict:
        character = self._cash_service.get(id)
        if not character:
            ...
        return character

    def add_character(self, id: int, character) -> None:
        self._cash_service.add_or_update(id, character)

    def update_character(self, id: int, character) -> None:
        self._cash_service.add_or_update(id, character)

    def delete_character(self, id: int) -> None:
        self._cash_service.delete(id)
