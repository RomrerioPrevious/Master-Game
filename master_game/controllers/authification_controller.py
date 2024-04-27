from master_game.config import Logger
from master_game.services.user_service import UserService
from flask import render_template, request, redirect, jsonify, Blueprint
from master_game.models import User

app = Blueprint("auth", __name__)
service = UserService()


def form():
    return "/form.html"


@app.route("/auth", methods=["GET"])
def auth():
    return render_template("/authenticate.html")


@app.route("/auth", methods=["POST"])
def authenticate_user():
    data = request.form
    email = data["email"]
    password = data["password"]
    user = service.get_user_by_email(email)
    try:
        if hash_password(password) == user.password:
            response = jsonify({"message": "User authenticated"})
            response.set_cookie("user_id", user.id)
            return response
        else:
            return jsonify({"error": "Invalid password"})
    except Exception as ex:
        Logger.write_error(ex)


@app.route("/registration", methods=["GET"])
def register_page():
    return render_template("/registration.html")


@app.route("/registration", methods=["POST"])
def register_user():
    data = request.form
    email = data["email"]
    password = data["password"]
    user = service.get_user_by_email(email)
    if not user:
        password = hash_password(password)
        user = User(id=0, email=email, username=data["username"], password=password,
                    age=int(data["age"]), status="user", sheets=[])
        service.add_user(user)
        return jsonify({"message": "User registered successfully"})
    return jsonify({"error": "User with this email already exists"})


@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    service.get_user_by_id(user_id)


@app.route("/user", methods=["POST"])
def create_user():
    form()
    id = int(request.form["id"])
    age = int(request.form["age"])
    password = hash_password(request.form["password"])
    name = request.form["account_name"]
    email = request.form["email"]
    status = request.form["status"]
    service.add_user(User(id=id, username=name, email=email, age=age, password=password,
                          status=status, sheets=[]))


@app.route("/user/<int:user_id>", methods=["PATCH"])
def update_user(user_id):
    form()
    name = request.form["account_name"]
    email = request.form["email"]
    age = request.form["age"]
    password = request.form["password"]
    hashed_password = hash_password(password)
    service.update_user(
        User(id=user_id, username=name, email=email, age=age, password=hashed_password, status="", sheets=[]))


@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    service.delete_user(user_id)


def hash_password(password: str) -> int:
    hash_value = 0
    for char in password:
        hash_value = (hash_value << 5) - hash_value + ord(char)
        hash_value = hash_value & 0xFFFFFFFF
    return hash_value
