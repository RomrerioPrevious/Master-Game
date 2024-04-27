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
    character = CharacterSheet(
        id=10,
        name="Igor",
        classes=["f"],
        rase="n",
        maxHits=10,
        hits=10,
        stats=Stats(
            id=10,
            strength=10,
            dexterity=10,
            constitution=10,
            intelligence=10,
            wisdom=10,
            charisma=10,
        ),
        armorClass=1,
        equipment=[],
        weapons=[Weapon(
            name="os",
            damage=1000,
            typeOfDamage="ultra",
            distance=1000,
            weight=1
        )],
        armor=Armor(
            name="d",
            armorClass="21",
            hindranceToSecrecy=True,
            strengthRequirement=2,
            weight=1,
        ),
        skills=["gray"],
        featuresAndTraits=["gray"],
        skillBonus=2,
        inspiration=2,
        speed=30,
        magic=["gigant"]
    )
    service = CharacterService()
    service.add_character(character)
    socetio.run(app, allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    ic.configureOutput(prefix=Logger.info,
                       outputFunction=Logger.write_log)
    main()
