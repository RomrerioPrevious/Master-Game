from master_game.services.user_service import UserService
from master_game.models import User
from unittest import TestCase
import pytest


class TestUserService(TestCase):
    user_service = UserService()

    def test_get(self):
        user = self.user_service.get_user_by_id(1)

    def test_add(self):
        user = User(
            id=1,
            username="User",
            email="user@email.com",
            age=21,
            password=8642,
            status="USER",
            sheets=[]
        )
        self.user_service.add_user(user)

    def test_update(self):
        user = User(
            id=1,
            username="Name",
            email="user@email.com",
            age=21,
            password=8642,
            status="USER",
            sheets=[]
        )
        self.user_service.update_user(user)

    def test_delete(self):
        self.user_service.delete_user(1)
