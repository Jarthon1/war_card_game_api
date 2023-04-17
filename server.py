from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from war import war_card_game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///war_card_game.db'  # SQLite database file path
db = SQLAlchemy(app)

# Define a Game model to represent games in the database
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    winner = db.Column(db.String(20))
    game_data = db.Column(db.PickleType())

    def __init__(self, status, winner, game_data):
        self.status = status
        self.winner = winner
        self.game_data = game_data

# Define a Win model to represent win records in the database
class Player(db.Model):
    player = db.Column(db.String(20))
    wins = db.Column(db.Integer)

    def __init__(self, player, wins):
        self.player = player
        self.wins = wins

with app.app_context():
    db.create_all() # Create the database tables

@app.route('/games', methods=['POST'])
def start_game():
    game_id = Game.query.count() + 1  # Generate a new game ID
    game = war_card_game()
    game_data = Game(status='started', winner='N/A', game_data=game)  # Create a new game object
    db.session.add(game_data)  # Add the game to the database
    db.session.commit()  # Commit the changes to the database
    return jsonify({'message': f'Game {game_id} started!', 'game_id': game_id}), 201

@app.route('/games/<int:game_id>', methods=['POST'])
def run_game(game_id):
    game = Game.query.get(game_id)  # Get the game object by ID from the database
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    if game.status != 'started':
        return jsonify({'error': 'Game not playable'}), 409
    else:
        winner = game.game_data.play_game()
        game.winner = winner
        game.status = 'finished'
        db.session.commit()  # Commit the changes to the database
        return jsonify({'message': f'Game {game_id} finished!', 'winner': game.winner}), 201

@app.route('/games/<int:game_id>', methods=['GET'])
def get_game_status(game_id):
    game = Game.query.get(game_id)  # Get the game object by ID from the database
    if game:
        return jsonify({'status': game.status, 'winner': game.winner})
    else:
        return jsonify({'error': 'Game not found'}), 404

@app.route('/wins/<string:player>', methods=['GET'])
def get_history(player):
    win = Player.query.filter_by(player=player).first()  # Get the win record for the player from the database
    if win:
        return jsonify({'lifetime_wins': win.wins})
    else:
        return jsonify({'error': 'Player not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
