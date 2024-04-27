from flask import Blueprint, request, jsonify
from ariadne import graphql_sync, snake_case_fallback_resolvers, \
    load_schema_from_path, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL
from master_game.models.query import query

app = Blueprint("graphql", __name__)
schema = make_executable_schema(
    load_schema_from_path("resources/data/schemas/user.graphql"),
    query,
    snake_case_fallback_resolvers
)
explorer_html = ExplorerGraphiQL().html(None)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return explorer_html, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
    )
    status = 400
    if success:
        status = 200
    return jsonify(result), status
