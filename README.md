# war_card_game_api
This is the source code for an API which supports the initialization of games of the card game war and keeps a record of the history of scores.

The most relevent files are server.py which runs the RESTful API which will respond to war requests and war.py which handles the game logic itself.

Simply running server.py should start up the server assuming all necessary dependancies are installed.

Dependencies are listed in war_card_game_dependencies.yml and you can create the necessary 
conda environment by running the following command:
% conda env create -f war_card_game_dependencies.yml

Once you have set up your server you can use any RESTful service to send requests to the API

This server has the following endpoints:

POST /games - starts a new game between two default players and returns a game ID, a message indicating the game has started, and the names of the players.

POST /games/string:player1/vs/string:player2 - starts a new game between two specified players and returns a game ID, a message indicating the game has started, and the names of the players.

POST /games/int:game_id - plays a game with the specified game ID, updates the game status and winner in the database, updates the win record of the winner in the database, and returns a message indicating the game has finished and the name of the winner.

GET /games/int:game_id - retrieves the status and winner of a game with the specified game ID.

GET /wins/string:player - retrieves the number of lifetime wins of a player with the specified name.

POST /player/string:player_name - creates a new player with the specified name and returns a message indicating the player has been created.




