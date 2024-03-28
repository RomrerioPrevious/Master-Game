from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/pers', methods=['POST'])
def create_character():
    pass


@app.route('/pers/<int:char_id>', methods=['PATCH'])
def update_character(char_id):
    pass


@app.route('/pers/<int:char_id>', methods=['DELETE'])
def delete_character(char_id):
    pass


@app.route('/pers/<int:char_id>', methods=['GET'])
def get_character(char_id):
    pass


@app.route('/class', methods=['GET'])
def get_classes():
    pass


@app.route('/species', methods=['GET'])
def get_species():
    pass


@app.route('/random', methods=['GET'])
def get_random_character():
    pass


@app.route('/random/cube', methods=['GET'])
def roll_cube():
    pass


@app.route('/random/items', methods=['GET'])
def get_random_items():
    pass
