from master_game.services.cache_service import CacheService
from master_game.models import CharacterSheet


class CharacterService:
    def __init__(self):
        self.cash_service = CacheService()

    def get_character(self, id: int) -> CharacterSheet:
        character = self.cash_service.get_character(id)
        if not character:
            ...
        return character

    def add_or_update_character(self, id: int, character: CharacterSheet) -> None:
        self.cash_service.add_or_update_character(id, character)

    def delete_character(self, id: int) -> None:
        self.cash_service.delete_user(id)

