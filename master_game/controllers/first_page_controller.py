from flask import Blueprint

app = Blueprint("first_page", __name__)


@app.route("/", methods=["GET"])
def index():
    return "Start page"
