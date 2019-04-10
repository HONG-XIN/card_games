from card import *
from deck import Deck
from player import Player
from dealer import Dealer

class Game:

	def __init__(self):
		self.you = Player()
		self.dealer = Dealer()
		self.deck = None

	def start(self):
		pass

	def get_winner(self):
		pass

	def if_end(self):
		pass

	def get_you_cards(self):
		return self.you.get_cards_on_hand()

	def get_dealer_cards(self):
		return self.dealer.get_cards_on_hand()

	def _clear_variables(self):
		self.you = Player()
		self.dealer = Dealer()
		self.deck = None

	def _deck_shuffle(self):
		self.deck.shuffle()
