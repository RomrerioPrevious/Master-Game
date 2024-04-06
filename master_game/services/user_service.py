from master_game.services.cache_service import CacheService
from .database_service import DatabaseService
from master_game.config import DATABASE_URL


class UserService:
    _database_service = None
    _cash_service = None
    _session = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserService, cls).__new__(cls)
            cls._database_service = DatabaseService(DATABASE_URL)
            cls._session = cls._database_service.get_session()
            cls._cash_service = CacheService()
        return cls.instance

    def get_user(self, id: int) -> dict:
        user = self._cash_service.get(id)
        if not user:
            ...  # TODO create database work
        return user.to_dict()

    def add_user(self, id: int, user) -> None:
        self._cash_service.add_or_update(id, user)
        self._session.add(user)
        if self._commit:
            self._session.commit()

    def update_user(self, id: int, user) -> None:
        self._cash_service.add_or_update(id, user)

    def delete_user(self, id: int) -> None:
        self._cash_service.delete(id)
        self._session.delete(self.get_user(id))
        if self._commit:
            self._session.commit()

    def commit(self) -> None:
        self._session.commit()
