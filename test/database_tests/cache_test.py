from master_game.services import CacheService
from master_game.models import User
from unittest import TestCase
import pytest


class TestCache(TestCase):
    cash_service = CacheService()

    def test_add_and_get_user_from_cash(self):
        user = User(
            id=1,
            username="Mike",
            email="a@gmail.com",
            age=22,
            password=648,
            avatar="",
            status="Player",
            sheets=None
        )
        self.cash_service.add_or_update_user(1, user)
        new_user = self.cash_service.get_user(1)
        assert user is new_user

    def test_delete_user_when_overflow(self):
        for i in range(1050):
            user = User(
                id=i,
                username="Mike",
                email="a@gmail.com",
                age=22,
                password=648,
                avatar="",
                status="Player",
                sheets=None
            )
            self.cash_service.add_or_update_user(i, user)
        assert self.cash_service.get_user(1) is None

    def test_get_user_when_overflow(self):
        for i in range(1050):
            user = User(
                id=i,
                username="Mike",
                email="a@gmail.com",
                age=22,
                password=648,
                avatar="",
                status="Player",
                sheets=None
            )
            self.cash_service.add_or_update_user(i, user)
        assert not self.cash_service.get_user(1000) is None
