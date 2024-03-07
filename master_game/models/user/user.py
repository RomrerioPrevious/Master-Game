from graphene import ObjectType, ID, Int, String
from dataclasses import dataclass


@dataclass
class User(ObjectType):
    id = ID
