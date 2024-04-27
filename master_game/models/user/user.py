from typing import Any

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, PickleType
from sqlalchemy.ext.mutable import MutableList
from master_game.services import DatabaseService


class User(DatabaseService.base):
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    age = Column(Integer)
    password = Column(Integer)
    status = Column(String)
    sheets = Column(MutableList.as_mutable(PickleType),
                    ForeignKey("characters.id"),
                    nullable=True,
                    default=[])

    @staticmethod
    def dict_to_user(self, dict_user: dict) -> Any:
        return User(
            id=dict_user["id"],
            username=dict_user["username"],
            email=dict_user["email"],
            age=dict_user["age"],
            password=dict_user["password"],
            status=dict_user["status"],
            sheets=dict_user["sheets"]
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "password": self.password,
            "status": self.status,
            "sheets": self.sheets
        }
