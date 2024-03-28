from master_game.services.cache_service import CacheService
from master_game.models.character import CharacterSheet


class CharacterService:
    def __init__(self):
        self._cash_service = CacheService()

    def get_character(self, id: int) -> CharacterSheet:
        character = self._cash_service.get(id)
        if not character:
            ...
        return character

    def add_or_update_character(self, id: int, character: CharacterSheet) -> None:
        self._cash_service.add_or_update(id, character)

    def delete_character(self, id: int) -> None:
        self._cash_service.delete(id)
