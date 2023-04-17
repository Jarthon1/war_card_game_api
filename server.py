# This is the File that sets up and manages the RESTful server supporting the card game War.
from flask import Flask, jsonify, request

app = Flask(__name__)

games = []  # List to store game information

@app.route('/games', methods=['POST'])  # Define a new endpoint for starting a game with POST method
def start_game():
    game_id = len(games) + 1  # Generate a new game ID
    game = {'id': game_id, 'status': 'started', 'history': []}  # Create a new game object
    games.append(game)  # Add the game to the games list
    return jsonify({'message': f'Game {game_id} started!', 'game_id': game_id}), 201  # Return a JSON response with game ID and message

@app.route('/games/<int:game_id>', methods=['GET'])  # Define a new endpoint for getting game history with GET method
def get_game_history(game_id):
    game = get_game_by_id(game_id)  # Get the game object by ID
    if game:
        return jsonify({'history': game['history']})  # Return the game's history as JSON response
    else:
        return jsonify({'error': 'Game not found'}), 404  # Return an error message if game not found

def get_game_by_id(game_id):
    for game in games:  # Iterate through games list to find game with matching ID
        if game['id'] == game_id:
            return game  # Return the game object if found
    return None  # Return None if game not found

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask app in debug mode for development
