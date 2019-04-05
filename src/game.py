from card import *
from deck import Deck

class Game:

	def __init__(self):
		self.you = []
		self.dealer = []
		self.deck = None

	def deck_draw_one(self):
		self.you.append(self.deck.draw())

	def start(self):
		pass

	def get_winner(self):
		pass

	def if_end(self):
		pass

	def get_you_cards(self):
		return self.you

	def get_dealer_cards(self):
		return self.dealer

	def _clear_variables(self):
		self.you = []
		self.dealer = []
		self.deck = None

	def _deck_shuffle(self):
		self.deck.shuffle()
