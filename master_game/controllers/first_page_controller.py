from flask import Blueprint, render_template

app = Blueprint("first_page", __name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("/index.html")
