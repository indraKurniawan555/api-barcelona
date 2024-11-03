from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data awal pemain Barcelona dengan detail lebih lengkap
players = {
    "1": {
        "name": "Marc-André ter Stegen",
        "position": "Goalkeeper",
        "number": 1,
        "age": 31,
        "nationality": "Germany",
        "height": "187 cm",
        "weight": "85 kg",
        "contract_until": "2025-06-30"
    },
    "2": {
        "name": "Ronald Araújo",
        "position": "Defender",
        "number": 4,
        "age": 25,
        "nationality": "Uruguay",
        "height": "188 cm",
        "weight": "81 kg",
        "contract_until": "2026-06-30"
    },
    "3": {
        "name": "Pedri",
        "position": "Midfielder",
        "number": 8,
        "age": 21,
        "nationality": "Spain",
        "height": "174 cm",
        "weight": "60 kg",
        "contract_until": "2028-06-30"
    },
    "4": {
        "name": "Frenkie de Jong",
        "position": "Midfielder",
        "number": 21,
        "age": 26,
        "nationality": "Netherlands",
        "height": "180 cm",
        "weight": "74 kg",
        "contract_until": "2026-06-30"
    },
    "5": {
        "name": "Robert Lewandowski",
        "position": "Forward",
        "number": 9,
        "age": 35,
        "nationality": "Poland",
        "height": "185 cm",
        "weight": "81 kg",
        "contract_until": "2025-06-30"
    }
}

# Classes for CRUD functionality as in previous example
class PlayerList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(players),
            "players": players
        }

class PlayerDetail(Resource):
    def get(self, player_id):
        if player_id in players:
            return {
                "error": False,
                "message": "Success",
                "player": players[player_id]
            }
        return {"error": True, "message": "Player not found"}, 404

class AddPlayer(Resource):
    def post(self):
        data = request.get_json()
        player_id = str(len(players) + 1)
        new_player = {
            "name": data.get("name"),
            "position": data.get("position"),
            "number": data.get("number"),
            "age": data.get("age"),
            "nationality": data.get("nationality"),
            "height": data.get("height"),
            "weight": data.get("weight"),
            "contract_until": data.get("contract_until")
        }
        players[player_id] = new_player
        return {
            "error": False,
            "message": "Player added successfully",
            "player": new_player
        }, 201

class UpdatePlayer(Resource):
    def put(self, player_id):
        if player_id in players:
            data = request.get_json()
            player = players[player_id]
            player["name"] = data.get("name", player["name"])
            player["position"] = data.get("position", player["position"])
            player["number"] = data.get("number", player["number"])
            player["age"] = data.get("age", player["age"])
            player["nationality"] = data.get("nationality", player["nationality"])
            player["height"] = data.get("height", player["height"])
            player["weight"] = data.get("weight", player["weight"])
            player["contract_until"] = data.get("contract_until", player["contract_until"])
            return {
                "error": False,
                "message": "Player updated successfully",
                "player": player
            }
        return {"error": True, "message": "Player not found"}, 404

class DeletePlayer(Resource):
    def delete(self, player_id):
        if player_id in players:
            deleted_player = players.pop(player_id)
            return {
                "error": False,
                "message": "Player deleted successfully",
                "player": deleted_player
            }
        return {"error": True, "message": "Player not found"}, 404

# Define the routes
api.add_resource(PlayerList, '/players')
api.add_resource(PlayerDetail, '/players/<string:player_id>')
api.add_resource(AddPlayer, '/players/add')
api.add_resource(UpdatePlayer, '/players/update/<string:player_id>')
api.add_resource(DeletePlayer, '/players/delete/<string:player_id>')

if __name__ == '__main__':
    app.run(debug=True)
