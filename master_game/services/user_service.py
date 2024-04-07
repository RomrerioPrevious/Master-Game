from master_game.services.cache_service import CacheService
from .database_service import DatabaseService
from master_game.models import User


class UserService:
    _database_service = None
    _cash_service = None
    _session = None
    commit = True

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserService, cls).__new__(cls)
            cls._database_service = DatabaseService()
            cls._session = cls._database_service.get_session()
            cls._cash_service = CacheService()
        return cls.instance

    def get_user(self, id: int) -> User:
        user = self._cash_service.get(id)
        if not user:
            user = self._session.query(User).filter(User.id == id).first()
        if not user:
            raise Exception(f"Not found user with id={id}")
        self._cash_service.add(user.id, user)
        return user

    def add_user(self, user: User) -> None:
        self._session.add(user)
        if self.commit:
            self._session.commit()

    def update_user(self, user) -> None:
        self._session.delete(user)
        self.add_user(user)
        if self.commit:
            self._session.commit()

    def delete_user(self, id: int) -> None:
        self._cash_service.delete(id)
        user = self.get_user(id=id)
        self._session.delete(user)
        if self.commit:
            self._session.commit()

