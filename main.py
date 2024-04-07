from icecream import ic
from master_game.config import Logger
from master_game.config import *
from master_game.services import DatabaseService
from master_game.controllers.graphql_controller import app


def main() -> None:
    ic("Master-game has been started")
    DatabaseService.init_base()
    app.run()


if __name__ == "__main__":
    ic.configureOutput(prefix=Logger.info,
                       outputFunction=Logger.write_log)
    main()
