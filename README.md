# war_card_game_api
This is the source code for an API which supports the initialization of games of the card game war and keeps a record of the history of scores.

The most relevent files are server.py which runs the RESTful API which will respond to war requests and war.py which handles the game logic itself.

Simply running server.py should start up the server assuming all necessary dependancies are installed.

Dependencies are listed in war_card_game_dependencies.yml and you can create the necessary 
conda environment by running the following command:
% conda env create -f war_card_game_dependencies.yml


