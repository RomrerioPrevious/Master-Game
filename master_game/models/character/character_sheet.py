from sqlalchemy import Column, Integer, String, ForeignKey, PickleType
from sqlalchemy.ext.mutable import MutableList
from master_game.services import DatabaseService


class CharacterSheet(DatabaseService.base):
    __tablename__ = "characters"

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    name = Column(String)
    classes = Column(MutableList.as_mutable(PickleType),
                     nullable=True,
                     default=[])
    rase = Column(String,
                  nullable=True)
    maxHits = Column(Integer,
                     nullable=True)
    hits = Column(Integer,
                  nullable=True)
    stats = Column(Integer,
                   ForeignKey("characters_stats.id"),
                   nullable=True)
    armorClass = Column(Integer,
                        nullable=True)
    equipment = Column(MutableList.as_mutable(PickleType),
                       nullable=True,
                       default=[])
    weapons = Column(MutableList.as_mutable(PickleType),
                     ForeignKey("weapons.id"),
                     nullable=True,
                     default=[])
    armor = Column(Integer,
                   ForeignKey("armors.id"),
                   nullable=True,
                   default=[])
    skills = Column(MutableList.as_mutable(PickleType),
                    nullable=True,
                    default=[])
    featuresAndTraits = Column(MutableList.as_mutable(PickleType),
                               nullable=True,
                               default=[])
    skillBonus = Column(Integer,
                        nullable=True)
    inspiration = Column(Integer,
                         nullable=True)
    speed = Column(Integer,
                   nullable=True)
    magic = Column(MutableList.as_mutable(PickleType),
                   nullable=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "classes": self.classes,
            "rase": self.rase,
            "maxHits": self.maxHits,
            "hits": self.hits,
            "stats": self.stats,
            "armorClass": self.armorClass,
            "equipment": self.equipment,
            "weapons": self.weapons,
            "armor": self.armor,
            "skills": self.skills,
            "featuresAndTraits": self.featuresAndTraits,
            "skillBonus": self.skillBonus,
            "inspiration": self.inspiration,
            "speed": self.speed,
            "magic": self.magic
        }
