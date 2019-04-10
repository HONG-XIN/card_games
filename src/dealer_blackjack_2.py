from dealer_blackjack import Dealer_Blackjack

class Dealer_Blackjack_2(Dealer_Blackjack):

	def __init__(self):
		super().__init__()
		self.difficulty = 2
		self.compare_number = 16

	def get_if_draw(self):
		return True if self.get_score() <= self.compare_number else False

	def set_init(self):
		self.difficulty = 2
		self.compare_number = 16
