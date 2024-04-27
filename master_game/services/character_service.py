from icecream import ic
from master_game.models import CharacterSheet, Weapon, Armor
from master_game.services import DatabaseService
from master_game.services.cache_service import CacheService


class CharacterService:
    _database_service = None
    _cash_service = None
    _session = None
    commit = True

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(CharacterService, cls).__new__(cls)
            cls._database_service = DatabaseService()
            cls._session = cls._database_service.get_session()
            cls._cash_service = CacheService()
        return cls.instance

    def get_character(self, id: int) -> CharacterSheet:
        character = self._cash_service.get(id)
        if not character:
            character = self._session.query(CharacterSheet)\
                .filter(CharacterSheet.id == id).first()
        if not character:
            raise Exception(f"Not found character with id={id}")
        self._cash_service.add(character.id, character)
        get = f"character with id={character.id}"
        ic(get)
        return character

    def add_character(self, character: CharacterSheet) -> None:
        armor = character.armor
        character.armor = armor.id
        stats = character.stats
        character.stats = stats.id
        weapons = character.weapons
        weapons_ids = []
        for i in weapons:
            weapons_ids.append(i.id)
            self._session.add(i)
        character.weapons = weapons_ids
        self._session.add(character)
        self._session.add(armor)
        self._session.add(stats)
        if self.commit:
            self._session.commit()
        add = character.to_dict()
        ic(add)

    def update_character(self, character: CharacterSheet) -> None:
        self._session.query(CharacterSheet)\
            .filter(CharacterSheet.id == int(character.id))\
            .update(character)
        if self.commit:
            self._session.commit()
        update = character.to_dict()
        ic(update)

    def delete_character(self, id: int) -> None:
        self._cash_service.delete(id)
        character = self.get_character(id=id)
        self._session.delete(character)
        if self.commit:
            self._session.commit()
        delete = f"user with id={character.id}"
        ic(delete)

    def get_characters_weapon_id(self, weapon: Weapon) -> int:
        charactersWeapon = weapon.to_dict()
        name, typeOfDamage = charactersWeapon["name"], charactersWeapon["typeOfDamage"]
        damage, distance, weight = charactersWeapon["damage"], charactersWeapon["distance"], charactersWeapon["weight"]
        hashedName = CharacterService.hashing_string(name)
        hashedTOD = CharacterService.hashing_string(name, 19_999_999)
        hashedId = hashedName + hashedTOD + (damage ^ weight) + round(distance / 10)  # убрать ^ ?
        return hashedId  # [0;2_147_483_647]

    def get_characters_armor_id(self, armor: Armor) -> int:
        charactersWeapon = armor.to_dict()
        name, armorClass = charactersWeapon["name"], charactersWeapon["armorClass"]
        hindranceToSecrecy = int(charactersWeapon["hindranceToSecrecy"])
        strengthRequirement, weight = charactersWeapon["strengthRequirement"], charactersWeapon["weight"]
        hashedId = hindranceToSecrecy * (2_147_483_646 // 2)
        hashedName = CharacterService.hashing_string(name, 2 - hindranceToSecrecy)
        hashedAC = CharacterService.hashing_string(armorClass, 1_999_999)
        hashedId += hashedName + hashedAC + strengthRequirement + weight
        return hashedId  # [0;2_147_483_647]

    @staticmethod
    def hashing_string(string, thresholdCoeff=1) -> int:
        hashed = 2_147_483_647
        billet = ""
        symbolsCodes = [code for code in map(ord, string)]
        for c in symbolsCodes:
            billet += str(c)
        while hashed > 2_000_000_000 // (1 + thresholdCoeff):
            hbl = len(billet) // 2
            hashed = int(billet[:hbl]) ^ int(billet[hbl:])
            billet = str(hashed)
        return hashed
