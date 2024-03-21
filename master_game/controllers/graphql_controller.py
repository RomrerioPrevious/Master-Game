from flask import Flask

app = Flask(__name__)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    ...


@app.route("/graphql", methods=["POST"])
def graphql_server():
    ...
