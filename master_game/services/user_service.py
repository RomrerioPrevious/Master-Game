from icecream import ic
from master_game.services.cache_service import CacheService
from .database_service import DatabaseService
from master_game.models import User


class UserService:
    _database_service = None
    _cash_service = None
    _session = None
    commit = True

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(UserService, cls).__new__(cls)
            cls._database_service = DatabaseService()
            cls._session = cls._database_service.get_session()
            cls._cash_service = CacheService()
        return cls.instance

    def get_user_by_id(self, id: int) -> User:
        user = self._cash_service.get(id)
        if not user:
            user = self._session.query(User).filter(User.id == id).first()
        if not user:
            raise Exception(f"Not found user with id={id}")
        self._cash_service.add(user.id, user)
        get = f"user with id={user.id}"
        ic(get)
        return user

    def get_user_by_email(self, email: str) -> User:
        user = self._session.query(User).filter(User.email == email).first()
        if not user:
            raise Exception(f"Not found user with id={id}")
        self._cash_service.add(user.id, user)
        get = f"user with id={user.id}"
        ic(get)
        return user

    def add_user(self, user: User) -> None:
        self._session.add(user)
        if self.commit:
            self._session.commit()
        add = user.to_dict()
        ic(add)

    def update_user(self, new_user) -> None:
        user = self.get_user_by_id(new_user.id)
        user.age = new_user.age
        user.email = new_user.email
        user.password = new_user.password
        user.username = new_user.username
        user.status = new_user.status
        user.sheets = new_user.sheets
        if self.commit:
            self._session.commit()
        update = user.to_dict()
        ic(update)

    def delete_user(self, id: int) -> None:
        self._cash_service.delete(id)
        user = self.get_user_by_id(id=id)
        self._session.delete(user)
        if self.commit:
            self._session.commit()
        delete = f"user with id={user.id}"
        ic(delete)

