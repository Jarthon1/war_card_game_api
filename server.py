# This is the File that sets up and manages the RESTful server supporting the card game War.
from flask import Flask, jsonify, request

from war import war_card_game

app = Flask(__name__)

games = []  # List to store game information

@app.route('/games', methods=['POST'])  # Define a new endpoint for setting up a game with POST method
def start_game():
    game_id = len(games) + 1  # Generate a new game ID
    game = war_card_game()
    game_data = {'id': game_id, 'status': 'started', 'game': game, 'winner':'N/A'}  # Create a new game object
    games.append(game_data)  # Add the game to the games list
    return jsonify({'message': f'Game {game_id} started!', 'game_id': game_id}), 201  # Return a JSON response with game ID and message

@app.route('/games/<int:game_id>', methods=['POST'])  # Define a new endpoint for actually running a game with POST method
def run_game(game_id):
    game = get_game_by_id(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404 # Return an error message (conflict) if gamestate is not playable
    if game['status'] != 'started':
        return jsonify({'error': 'Game not playable'}), 409 # Return an error message (conflict) if gamestate is not playable
    else:
        winner = game['game'].play_game()
        print(winner)
        game['winner'] = winner
        game['status'] = 'finished'
        return jsonify({'message': f'Game {game_id} finished!', 'winner': game['winner']}), 201  # Return a JSON response with game ID and message
        
@app.route('/games/<int:game_id>', methods=['GET'])  # Define a new endpoint for getting game history with GET method
def get_game_status(game_id):
    game = get_game_by_id(game_id)  # Get the game object by ID
    if game:
        return jsonify({'status': game['status'], 'winner': game['winner']})  # Return the game's history as JSON response
    else:
        return jsonify({'error': 'Game not found'}), 404  # Return an error message if game not found

# Retrieve a game by its id
def get_game_by_id(game_id):
    for game in games:  # Iterate through games list to find game with matching ID
        if game['id'] == game_id:
            return game  # Return the game object if found
    return None  # Return None if game not found

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask app in debug mode for development
