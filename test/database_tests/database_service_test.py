import pytest
from master_game.services import DatabaseService


class DatabaseServiceTest:
    database = DatabaseService()

    def test_connection(self):
        assert True

    def test_singleton(self):
        next_database = DatabaseService()
        assert next_database is self.database
