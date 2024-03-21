from sqlalchemy.orm import sessionmaker
from master_game.services.cache_service import CacheService
from master_game.models import User
from sqlalchemy import create_engine, update


class UserService:
    _cash_service = None
    _session = None
    _engine = None

    def __init__(self):
        if not self._engine:
            self._engine = create_engine("sqlite:///resources/data/users.db", echo=True)
            self._cash_service = CacheService()
            Session = sessionmaker(bind=self._engine)
            self._session = Session()

    def get_user(self, id: int) -> User:
        user = self._cash_service.get_user(id)
        if not user:
            user = self._session.get(User, None)
        return user

    def add_or_update_user(self, id: int, user: User) -> None:
        self._cash_service.add_or_update_user(id, user)
        if user in self.get_user(id):
            self._session.add(user)
        else:
            self._session.query().update()

    def delete_user(self, id: int) -> None:
        self._cash_service.delete_user(id)
        self._session.delete(self.get_user(id))

    def commit(self) -> None:
        self._session.commit()
