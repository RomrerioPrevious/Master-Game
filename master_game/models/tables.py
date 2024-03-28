from sqlalchemy import Column, Integer, String, ForeignKey, PickleType, Boolean


class UserTable:
    __tablename__ = "users"

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    age = Column(Integer)
    password = Column(Integer)
    status = Column(String)
    sheets = Column(PickleType,
                    ForeignKey("characters.id"),
                    nullable=True)


class CharacterTable:
    __tablename__ = "characters"

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    name = Column(String)
    classes = Column(PickleType,
                     nullable=True)
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
    equipment = Column(PickleType,
                       nullable=True)
    weapons = Column(PickleType,
                     ForeignKey("weapons.id"),
                     nullable=True)
    armor = Column(Integer,
                   ForeignKey("armors.id"),
                   nullable=True)
    skills = Column(PickleType,
                    nullable=True)
    featuresAndTraits = Column(PickleType,
                               nullable=True)
    skillBonus = Column(Integer,
                        nullable=True)
    inspiration = Column(Integer,
                         nullable=True)
    speed = Column(Integer,
                   nullable=True)
    magic = Column(PickleType,
                   nullable=True)


class StatsTable:
    __tablename__ = "stats"

    id = Column(Integer,
                primary_key=True, autoincrement=True)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)


class ArmorTable:
    __tablename__ = "armors"

    id = Column(Integer,
                primary_key=True)
    armorClass = Column(String)
    hindranceToSecrecy = Column(Boolean)
    strengthRequirement = Column(Integer)
    weight = Column(Integer)
    counter = Column(Integer)


class WeaponTable:
    __tablename__ = "weapons"

    id = Column(Integer,
                primary_key=True)
    damage = Column(Integer)
    typeOfDamage = Column(String)
    distance = Column(Integer)
    weight = Column(Integer)
    counter = Column(Integer)
