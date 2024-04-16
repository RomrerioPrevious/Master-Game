from flask import Blueprint, render_template, redirect, request
from flask_socketio import SocketIO, join_room, leave_room, emit, send

from master_game.models.room import Room
from master_game.services.room_service import RoomService
from master_game.services.character_service import CharacterService
from master_game.services.user_service import UserService
from random import randint
from icecream import ic

app = Blueprint("game", __name__)

socetio = SocketIO()
room_service = RoomService()
character_service = CharacterService()
user_service = UserService()


@app.route("/game", methods=["POST"])
def create_room():
    room_id = randint(0, 2_000_000_000)
    user_id = int(request.cookies["user_id"])
    while room_id not in room_service.get_active_ids():
        room_id = randint(0, 2_000_000_000)
    room_service.create_room(room_id, user_id)
    return redirect(f"/game")


@app.route("/game", methods=["GET"])
def game():
    return render_template("/game.html")


@socetio.on("join", namespace="/game")
def join(data):
    room_id = data["room_id"]
    if room_id not in room_service.get_active_ids():
        return redirect("/game")
    room = room_service.get_room(room_id)
    room["users"][data["user_id"]](
        {"status": "player"}
    )
    join_room(room_id)
    ic(room_id, data["user_id"])
    return render_template("/game.html")


@socetio.on("add_character", namespace="/game")
def add_character(data):
    room_id = data["room"]
    x, y = data["coordinates"]
    character_id = data["character"]
    user_id = data["user"]
    room = room_service.get_room(room_id)
    character = None
    if verify_character(user_id, character_id, room):
        character = room["characters"][character_id]
        character["coordinates"] = (x, y)
        room["characters"][character_id] = character
    msg = character
    ic(room_id, msg)


@socetio.on("push_character", namespace="/game")
def push(data):
    room_id = data["room"]
    x, y = data["coordinates"]
    character_id = data["character"]
    user_id = data["user"]
    room = room_service.get_room(room_id)
    character = room["characters"][character_id]
    if verify_character(user_id, character_id, room):
        character["coordinates"] = (x, y)
    msg = character
    ic(room_id, msg)
    emit("push", {**msg}, room=room_id)


@socetio.on("damage", namespace="/game")
def damage(data):
    room_id = data["room"]
    character_id = data["character"]
    user_damage_id = data["user"]
    damage = data["damage"]
    room = room_service.get_room(room_id)
    if user_damage_id in room["users"].keys():
        character = character_service.get_character(character_id)
        if character.hits - damage <= 0:
            character.hits = 0
        else:
            character.hits -= damage
        character_service.update_character(character)


@socetio.on("leave", namespace="/game")
def leave(data):
    room_id = data["room"]
    user_id = data["user"]
    room = room_service.get_room(room_id)
    leave_room(room_id)
    if not room["users"] or room["users"][user_id]["status"] == "master":
        room_service.close_room(room_id)
        leave = f"Room {room_id} closed"
        ic(leave)
    leave = f"User {user_id} leave from room {room_id}"
    ic(leave)


def verify_character(user_id: int, character_id: int, room: Room) -> bool:
    if user_id in room["users"].keys():
        sheets = user_service.get_user(user_id).sheets
        if character_id in list(map(lambda sheet: sheet.id, sheets)):
            return True
    return False
