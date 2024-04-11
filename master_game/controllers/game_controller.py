from flask import Blueprint, render_template, redirect
from flask_socketio import SocketIO, join_room, leave_room
from icecream import ic

app = Blueprint("game", __name__)

socetio = SocketIO()


@app.route("/game", methods=["POST"])
def create():
    ...


@socetio.on("join", namespace="/game/<int:room_id>")
def join(room_id: int, data):
    return render_template("resources/pages/game.html")


@socetio.on("push_character", namespace="/game/<int:room_id>")
def push(room_id: int):
    ...


@socetio.on("", namespace="game/<int:room_id>")
def damage(room_id: int):
    ...
