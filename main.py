from icecream import ic
from master_game.config import Logger
from flask import Flask
from master_game.config import *
from master_game.services import DatabaseService
from master_game.controllers import graphql_controller as graphql, \
    first_page_controller as first_page, game_controller as game, \
    character_controller as character, authification_controller as auth

app = Flask(__name__,
            template_folder="resources/pages")
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
    socetio.run(app, allow_unsafe_werkzeug=True)


if __name__ == "__main__":
    ic.configureOutput(prefix=Logger.info,
                       outputFunction=Logger.write_log)
    main()
