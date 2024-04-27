from flask import Blueprint, render_template, request

app = Blueprint("first_page", __name__)


@app.route("/", methods=["GET"])
def index():
    user_id = request.cookies.get("user_id")
    return render_template("/index.html", user=user_id)
