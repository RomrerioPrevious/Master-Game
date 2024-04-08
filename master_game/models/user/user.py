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
