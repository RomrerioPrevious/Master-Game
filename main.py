from icecream import ic
from master_game.config import Logger
from flask import Flask
from master_game.config import *
from master_game.models import CharacterSheet, Stats, Weapon, Armor
from master_game.services import DatabaseService
from master_game.controllers import graphql_controller as graphql, \
    first_page_controller as first_page, game_controller as game, \
    character_controller as character, authification_controller as auth
from master_game.services.character_service import CharacterService

app = Flask(__name__,
            template_folder="resources/pages",
            static_folder="resources/pages")
app.config["SECRET_KEY"] = "RSQ_ET-eHvsI5u0Z-mwFk-MVRwADSb"

blueprints = [
    graphql.app,
    first_page.app,
    game.app,
    auth.app,
    character.app
]


def main() -> None:
    ic("Master-game has been started")
    for bluprint in blueprints:
        app.register_blueprint(bluprint)
    DatabaseService.init_base()
    socetio = game.socetio
    socetio.init_app(app)
    service = CharacterService()
    character = CharacterSheet(
        id=0,
        name="F",
        classes=["Engineer"],
        rase="",
        maxHits=10,
        hits=10,
        stats=Stats(
            id=0,
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10
        ),
        armorClass=1,
        equipment=["n", "b"],
        weapons=[Weapon(
            id=1,
            name="1",
            damage=2,
            typeOfDamage="big",
            distance=120,
            weight=1,
            counter=1,
        )],
        armor=Armor(
            id=1,
            name="n",
            armorClass=12,
            hindranceToSecrecy=True,
            strengthRequirement=1,
            weight=1,
            counter=1
        ),
        skills=["1"],
        featuresAndTraits=["norm"],
        skillBonus=2,
        inspiration=1,
        speed=30,
        magic=["d"],
    )
    service.add_character(character)
    socetio.run(app, allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    ic.configureOutput(prefix=Logger.info,
                       outputFunction=Logger.write_log)
    main()
