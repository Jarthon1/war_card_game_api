# This is a File containing the logic for the game of war
from copy import *
from random import *
import numpy as np
import itertools
import time

# GLOBAL VARIABLES

# GAMESTATE:
game_over = False
watch_mode = False

# Suit, (Hex Letter Ranking if it is a face card), Symbol 
# e.g: Ace of spades: 'SAA'
DECK = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','CAJ','CBQ','CCK','CDA',
		'D0','D1','D2','D3','D4','D5','D6','D7','D8','D9','DAJ','DBQ','DCK','DDA',
		'H0','H1','H2','H3','H4','H5','H6','H7','H8','H9','HAJ','HBQ','HCK','HDA',
		'S0','S1','S2','S3','S4','S5','S6','S7','S8','S9','SAJ','SBQ','SCK','SDA']

# Variables to store each players hand
P1_Deck = []
P2_Deck = []

# war decks:
P1_Temp = []
P2_Temp = []

# GAME LOGIC
# STEP 1 SETUP:

# first make a copy and shuffle the deck
play_deck = copy(DECK)

# shuffle the deck
np.random.shuffle(play_deck)

# each player gets half
P1_Deck = copy(play_deck[0:26])
P2_Deck = copy(play_deck[26:52])

# STEP 2 GAMEPLAY

# Gameplay Loop
while not game_over:
	p1_card = P1_Deck.pop(0)
	p2_card = P2_Deck.pop(0)

	# Reset war decks:
	P1_Temp = []
	P2_Temp = []

	# War logic
	while P1_Deck and P2_Deck and p1_card[1] == p2_card[1]:
		# game_over condition
		if len(P1_Deck) < 2 or len(P2_Deck) < 2 and not game_over:
			game_over = True
			if (len(P1_Deck) > len(P2_Deck)): 
				winner = 1 
			else: 
				winner = 2
			print(f"GAMEOVER !! Player {winner} won!\n")
			break

		P1_Temp.append(p1_card)
		P2_Temp.append(p2_card)

		P1_Temp.append(P1_Deck.pop(0))
		P2_Temp.append(P2_Deck.pop(0))

		p1_card = P1_Deck.pop(0)
		p2_card = P2_Deck.pop(0)

	if p1_card[1] > p2_card[1]:
		P1_Deck = P1_Deck + P1_Temp
		P1_Deck = P1_Deck + P2_Temp
		P1_Deck.append(p2_card)
		P1_Deck.append(p1_card)
	else:
		P2_Deck = P2_Deck + P2_Temp
		P2_Deck = P2_Deck + P1_Temp
		P2_Deck.append(p1_card)
		P2_Deck.append(p2_card)

	if watch_mode:
		time.sleep(0.2)
		print(f"Player 1 has {len(P1_Deck)} cards left,\nPlayer 2 has {len(P2_Deck)} cards left\n\n")

	# game_over condition
	if not P1_Deck or not P2_Deck and not game_over:
		game_over == True
		if (len(P1_Deck) > len(P2_Deck)): 
			winner = 1 
		else: 
			winner = 2
		print(f"GAMEOVER !! Player {winner} won!\n")
		break






















