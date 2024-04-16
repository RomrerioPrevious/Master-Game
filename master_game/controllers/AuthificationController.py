import random
from flask import Flask, render_template, url_for, request
from user import User
from user_service import UserService

app = Flask(__name__)
service = UserService()


def hash_password(password):
    hash_value = 0
    for char in password:
        hash_value = (hash_value << 5) - hash_value + ord(char)
        hash_value = hash_value & 0xFFFFFFFF
    return hash_value


def form():
    return "/form.html"


@app.route('/auth', methods=['GET'])
def auth():
    # TODO: authentication
    return render_template("/page.html")


@app.route('/user', methods=['POST'])
def create_user():
    form()
    name = request.form["account_name"]
    email = request.form["email"]
    age = request.form["age"]
    password = request.form["password"]
    status = request.form["status"]
    id = random.randint(10000, 99999)
    # filled add_user as example, change later
    service.add_user(id,
                     User(id=id, username=name, email=email, age=int(age), password=hash_password(password),
                          status=status, sheets=[]))


@app.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    password = ""
    hash_value = 0
    for char in password:
        hash_value = (hash_value << 5) - hash_value + ord(char)
        hash_value = hash_value & 0xFFFFFFFF
    hashed_password = hash_value
    service.update_user(user_id,
                        User(id=user_id, username="", email="", age=0, password=hashed_password, status="", sheets=[]))


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    service.delete_user(user_id)


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    service.get_user(user_id)
