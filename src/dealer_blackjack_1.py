from dealer_blackjack import Dealer_Blackjack
from random import choice

class Dealer_Blackjack_1(Dealer_Blackjack):

	def __init__(self):
		super().__init__()
		self.difficulty = 1

	def get_if_draw(self):
		return choice([True, False])

	def set_init(self):
		self.difficulty = 1
