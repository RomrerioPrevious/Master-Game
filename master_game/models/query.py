from ariadne import QueryType
from graphql import GraphQLResolveInfo
from master_game.config import Logger
from master_game.services.user_service import UserService
from master_game.services.character_service import CharacterService

query = QueryType()
user_service = UserService()
character_service = CharacterService()


@query.field("user")
def user(self, info: GraphQLResolveInfo, id: int) -> dict:
    try:
        return user_service.get_user(id)
    except Exception as ex:
        Logger.write_error(ex)


@query.field("character")
def character(self, info: GraphQLResolveInfo, id: int) -> dict:
    try:
        return character_service.get_character(id)
    except Exception as ex:
        Logger.write_error(ex)
