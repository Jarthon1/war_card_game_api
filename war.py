# This is a File containing the logic for the game of war
from copy import *
from random import *
import numpy as np
import itertools
import time

# Suit, (Hex Letter Ranking if it is a face card), Symbol 
# e.g: Ace of spades: 'SAA'
DECK = ['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','CAJ','CBQ','CCK','CDA',
		'D0','D1','D2','D3','D4','D5','D6','D7','D8','D9','DAJ','DBQ','DCK','DDA',
		'H0','H1','H2','H3','H4','H5','H6','H7','H8','H9','HAJ','HBQ','HCK','HDA',
		'S0','S1','S2','S3','S4','S5','S6','S7','S8','S9','SAJ','SBQ','SCK','SDA']

# GAME LOGIC
class war_card_game:
	def __init__(self):
		# STEP 1 SETUP:
		# GAMESTATE:
		self.game_over = False
		self.watch_mode = False
		self.winner = None

		# war decks:
		self.P1_Temp = []
		self.P2_Temp = []

		# first make a copy of the deck and shuffle it
		self.play_deck = copy(DECK)

		# shuffle the deck
		np.random.shuffle(self.play_deck)

		# each player gets half
		self.P1_Deck = copy(self.play_deck[0:26])
		self.P2_Deck = copy(self.play_deck[26:52])

	# STEP 2 GAMEPLAY
	def play_game(self): # Plays a full game of war
		# Gameplay Loop
		while not self.game_over:
			self.play_turn()
		return self.winner()
	
	def play_turn(self, watch_mode = False): # plays the next turn of war
		# Take the top card from each deck
		p1_card = self.P1_Deck.pop(0)
		p2_card = self.P2_Deck.pop(0)

		# Reset war decks:
		self.P1_Temp = []
		self.P2_Temp = []

		# War logic
		# Continue playing the turn as long as both players have cards and the visible card is equal
		while self.P1_Deck and self.P2_Deck and p1_card[1] == p2_card[1]:
			# check if either player has too few cards to continue and if so assign the winner and end the turn
			if (len(self.P1_Deck) < 2 or len(self.P2_Deck) < 2) and not self.game_over:
				self.game_over = True
				if (len(self.P1_Deck) > len(self.P2_Deck)): 
					self.winner = 1 
				else: 
					self.winner = 2
				print(f"GAMEOVER !! Player {self.winner} won!\n")
				return
			
			# Otherwise add the current face up cards to the war decks
			self.P1_Temp.append(p1_card)
			self.P2_Temp.append(p2_card)

			# And then add another card from the top of your personal deck to the war decks
			self.P1_Temp.append(self.P1_Deck.pop(0))
			self.P2_Temp.append(self.P2_Deck.pop(0))

			# Finlly deal a new visible card to continue the war
			p1_card = self.P1_Deck.pop(0)
			p2_card = self.P2_Deck.pop(0)

		# Now that the current war has ended, give the winning player all cards from both war decks and the visible cards
		if p1_card[1] > p2_card[1]:
			self.P1_Deck += self.P1_Temp
			self.P1_Deck += self.P2_Temp
			self.P1_Deck.append(p2_card)
			self.P1_Deck.append(p1_card)
		else:
			self.P2_Deck += self.P2_Temp
			self.P2_Deck += self.P1_Temp
			self.P2_Deck.append(p1_card)
			self.P2_Deck.append(p2_card)

		# This prints out the current game state if watch_mode is true
		if watch_mode:
			time.sleep(0.2)
			print(f"Player 1 has {len(self.P1_Deck)} cards left,\nPlayer 2 has {len(self.P2_Deck)} cards left\n\n")

		# Now check if the game is over, and if so, update the winner accordingly
		if not self.P1_Deck or not self.P2_Deck and not self.game_over:
			self.game_over == True
			if (len(self.P1_Deck) > len(self.P2_Deck)): 
				self.winner = 'player1' 
			else: 
				self.winner = 'player2'
			print(f"GAMEOVER !! Player {self.winner} won!\n")
		return






















