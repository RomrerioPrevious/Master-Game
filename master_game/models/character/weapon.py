from sqlalchemy import Column, Integer, String
from master_game.services import DatabaseService


class Weapon(DatabaseService.base):
    __tablename__ = "weapons"

    id = Column(Integer,
                primary_key=True)
    name = Column(String)
    damage = Column(Integer)
    typeOfDamage = Column(String)
    distance = Column(Integer)
    weight = Column(Integer)
    counter = Column(Integer)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "damage": self.damage,
            "typeOfDamage": self.typeOfDamage,
            "distance": self.distance,
            "weight": self.weight,
            "counter": self.counter
        }
