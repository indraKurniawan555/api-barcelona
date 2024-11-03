from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)

# Data pemain Barcelona (sebagai contoh data)
players = [
    {"id": 1, "name": "Marc-André ter Stegen", "position": "Goalkeeper", "number": 1},
    {"id": 2, "name": "Ronald Araújo", "position": "Defender", "number": 4},
    {"id": 3, "name": "Andreas Christensen", "position": "Defender", "number": 15},
    {"id": 4, "name": "Jordi Alba", "position": "Defender", "number": 18},
    {"id": 5, "name": "Sergio Busquets", "position": "Midfielder", "number": 5},
    {"id": 6, "name": "Pedri", "position": "Midfielder", "number": 8},
    {"id": 7, "name": "Frenkie de Jong", "position": "Midfielder", "number": 21},
    {"id": 8, "name": "Ousmane Dembélé", "position": "Forward", "number": 7},
    {"id": 9, "name": "Robert Lewandowski", "position": "Forward", "number": 9},
    {"id": 10, "name": "Ansu Fati", "position": "Forward", "number": 10}
]

# Endpoint untuk mendapatkan semua pemain
@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players)

# Endpoint untuk mendapatkan pemain berdasarkan ID
@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    player = next((p for p in players if p["id"] == player_id), None)
    if player is None:
        abort(404, description="Player not found")
    return jsonify(player)

# Endpoint untuk menambah pemain baru
@app.route('/players', methods=['POST'])
def add_player():
    if not request.json or 
