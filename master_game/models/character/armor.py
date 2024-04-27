from sqlalchemy import Column, Integer, String, Boolean
from master_game.services import DatabaseService


class Armor(DatabaseService.base):
    __tablename__ = "armors"

    id = Column(Integer,
                primary_key=True)
    name = Column(String)
    armorClass = Column(String)
    hindranceToSecrecy = Column(Boolean)
    strengthRequirement = Column(Integer)
    weight = Column(Integer)
    counter = Column(Integer)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "armorClass": self.armorClass,
            "hindranceToSecrecy": self.hindranceToSecrecy,
            "strengthRequirement": self.strengthRequirement,
            "weight": self.weight,
            "counter": self.counter
        }
