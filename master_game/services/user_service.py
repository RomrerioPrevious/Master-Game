from sqlalchemy.orm import sessionmaker
from master_game.services.cache_service import CacheService
from master_game.models import User
from sqlalchemy import create_engine


class UserService:
    _cash_service = None
    _session = None
    _engine = None
    _commit = True

    def __init__(self):
        if not self._engine:
            self._engine = create_engine("sqlite:///resources/data/users.db", echo=True)
            self._cash_service = CacheService()
            Session = sessionmaker(bind=self._engine)
            self._session = Session()

    def get_user(self, id: int) -> User:
        user = self._cash_service.get(id)
        if not user:
            user = self._session.get(User, None)  # TODO create database work
        return user

    def add_user(self, id: int, user: User) -> None:
        self._cash_service.add_or_update(id, user)
        self._session.add(user)
        if self._commit:
            self._session.commit()

    def update_user(self, id: int, user: User) -> None:
        self._cash_service.add_or_update(id, user)

    def delete_user(self, id: int) -> None:
        self._cash_service.delete(id)
        self._session.delete(self.get_user(id))
        if self._commit:
            self._session.commit()

    def commit(self) -> None:
        self._session.commit()
