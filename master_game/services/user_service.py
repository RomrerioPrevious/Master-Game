from master_game.services.cache_service import CacheService
from master_game.models import User


class UserService:
    def __init__(self):
        self.cash_service = CacheService()

    def get_user(self, id: int) -> User:
        user = self.cash_service.get_user(id)
        if not user:
            ...
        return user

    def add_or_update_user(self, id: int, user) -> None:
        self.cash_service.add_or_update_user(id, user)

    def delete_user(self, id: int) -> None:
        self.cash_service.delete_user(id)
