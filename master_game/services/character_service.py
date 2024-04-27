from icecream import ic
from sqlalchemy import and_

from master_game.models import CharacterSheet, Weapon, Armor, Stats
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
            character = self._session.query(CharacterSheet) \
                .filter(CharacterSheet.id == id).first()
        if not character:
            raise Exception(f"Not found character with id={id}")
        self._cash_service.add(character.id, character)
        get = f"character with id={character.id}"
        ic(get)
        return character

    def add_character(self, character: CharacterSheet) -> None:
        self._add_armor(character)
        self._add_weapons(character)
        stats = character.stats
        character.stats = stats.id
        self._session.add(stats)
        self._session.add(character)
        if self.commit:
            self._session.commit()
        add = character.to_dict()
        ic(add)

    def _add_weapons(self, character):
        weapons = character.weapons
        weapons_ids = []
        for weapon in weapons:
            weapon_id = self.get_weapon_id(weapon)
            weapons_ids.append(weapon_id)
            if self._session.query(Weapon).filter(Weapon.id == weapon_id).first():
                weapon = self._session.query(Weapon).filter(Weapon.id == weapon_id).first()
                weapon.counter += 1
            else:
                weapon.id = weapon_id
                weapon.counter = 1
                self._session.add(weapon)
            self._session.add(weapon)
        character.weapons = weapons_ids

    def _add_armor(self, character: CharacterSheet):
        armor = character.armor
        armor_id = self.get_armor_id(armor)
        character.armor = armor_id
        if self._session.query(Armor).filter(Armor.id == armor_id).first():
            armor = self._session.query(Armor).filter(Armor.id == armor_id).first()
            armor.counter += 1
        else:
            armor.id = armor_id
            armor.counter = 1
            self._session.add(armor)
        return armor

    def update_character(self, new_character: CharacterSheet) -> None:
        character = self._session.query(CharacterSheet) \
            .filter(CharacterSheet.id == int(new_character.id)) \
            .first()
        self._update_weapons(new_character, character)
        self._update_armor(new_character, character)
        self._update_stats(new_character, character)
        self._update_character_fields(character, new_character)
        if self.commit:
            self._session.commit()
        update = character.to_dict()
        ic(update)

    def _update_character_fields(self, character, new_character):
        character.name = new_character.name
        character.classes = new_character.classes
        character.rase = new_character.rase
        character.maxHits = new_character.maxHits
        character.hits = new_character.hits
        character.armorClass = new_character.armorClass
        character.equipment = new_character.equipment
        character.skills = new_character.skills
        character.featuresAndTraits = new_character.featuresAndTraits
        character.skillBonus = new_character.skillBonus
        character.inspiration = new_character.inspiration
        character.speed = new_character.speed
        character.magic = new_character.magic

    def _update_stats(self, new_character, character):
        character.stats = new_character.stats.id
        stats = self._session.query(Stats).filter(Stats.id == int(new_character.id)).first()
        stats.wisdom = new_character.stats.wisdom
        stats.charisma = new_character.stats.charisma
        stats.strength = new_character.stats.strength
        stats.dexterity = new_character.stats.dexterity
        stats.constitution = new_character.stats.constitution
        stats.intelligence = new_character.stats.intelligence

    def _update_armor(self, new_character, character):
        armor = new_character.armor
        armor_id = self.get_armor_id(armor)
        if armor_id != character.armor:
            old_armor = self._session.query(Armor).filter(Armor.id == int(new_character.armor_id)).first()
            if not old_armor:
                armor.id = armor_id
                armor.counter = 1
                self._session.add(armor)
            elif old_armor.counter - 1 == 0:
                self._session.delete(old_armor)
            else:
                old_armor.counter += 1
        new_character.armor = armor_id

    def _update_weapons(self, new_character, character):
        ids = []
        for weapon in new_character.weapons:
            weapon_id = self.get_weapon_id(weapon)
            if weapon not in character.weapons:
                old_weapon = self._session.query(Weapon).filter(Weapon.id == weapon_id).first()
                if not old_weapon:
                    weapon.id = weapon_id
                    weapon.counter = 1
                    self._session.add(weapon)
                elif old_weapon.counter - 1 == 0:
                    self._session.delete(old_weapon)
                else:
                    old_weapon.counter += 1
            ids.append(weapon_id)
        new_character.weapons = ids

    def delete_character(self, id: int) -> None:
        self._cash_service.delete(id)
        character = self.get_character(id=id)
        for weapon_id in character.weapons:
            weapon = self._session.query(Weapon).filter(Weapon.id == int(weapon_id)).first()
            if not weapon:
                ic(weapon)
            elif weapon.counter - 1 == 0:
                self._session.delete(weapon)
            else:
                weapon.counter -= 1
        armor = self._session.query(Armor).filter_by(id=character.armor).first()
        if armor.counter - 1 == 0:
            self._session.delete(armor)
        else:
            armor.counter -= 1
        self._session.delete(character)
        if self.commit:
            self._session.commit()
        delete = f"user with id={character.id}"
        ic(delete)

    def get_weapon_id(self, weapon: Weapon) -> int:
        charactersWeapon = weapon.to_dict()
        name, typeOfDamage = charactersWeapon["name"], charactersWeapon["typeOfDamage"]
        damage, distance, weight = charactersWeapon["damage"], charactersWeapon["distance"], charactersWeapon["weight"]
        hashedName = CharacterService.hashing_string(name)
        hashedTOD = CharacterService.hashing_string(name, 19_999_999)
        hashedId = hashedName + hashedTOD + (damage ^ weight) + round(distance / 10)  # убрать ^ ?
        return hashedId  # [0;2_147_483_647]

    def get_armor_id(self, armor: Armor) -> int:
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
