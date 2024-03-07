from sqlalchemy.engine import create_engine
from master_game.config import GRAPHQL_URL


class DatabaseService:
    def __new__(cls):
        if not hasattr(cls, "engine"):
            cls.engine = create_engine(GRAPHQL_URL)
        return cls.engine