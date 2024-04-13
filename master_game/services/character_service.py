from icecream import ic
from master_game.models import CharacterSheet
from master_game.services import DatabaseService
from master_game.services.cache_service import CacheService


class CharacterService:
    _database_service = None
    _cash_service = None
    _session = None
    commit = True  # коммитит в общую базу данных

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CharacterService, cls).__new__(cls)
            cls._database_service = DatabaseService()
            cls._session = cls._database_service.get_session()
            cls._cash_service = CacheService()
        return cls.instance

    def get_character(self, id: int) -> CharacterSheet:
        character = self._cash_service.get(id)
        if not character:
            character = self._session.query(CharacterSheet).filter(CharacterSheet.id == id).first()
        if not character:
            raise Exception(f"Not found character with id={id}")
        self._cash_service.add(character.id, character)
        get = f"character with id={character.id}"
        ic(get)
        return character

    def add_character(self, character: CharacterSheet) -> None:
        self._session.add(character)
        if self.commit:
            self._session.commit()
        add = character.to_dict()
        ic(add)

    def update_character(self, character: CharacterSheet) -> None:
        self._session.delete(character)
        self.add_character(character)
        if self.commit:
            self._session.commit()
        update = character.to_dict()
        ic(update)

    def delete_character(self, id: int) -> None:
        self._cash_service.delete(id)
        character = self.get_character(id=id)
        self._session.delete(character)
        if self.commit:
            self._session.commit()
        delete = f"user with id={character.id}"
        ic(delete)

