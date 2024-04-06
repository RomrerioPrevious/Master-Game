from sqlalchemy import Column, Integer
from master_game.services import DatabaseService


class Stats(DatabaseService.base):
    __tablename__ = "stats"

    id = Column(Integer,
                primary_key=True)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }
