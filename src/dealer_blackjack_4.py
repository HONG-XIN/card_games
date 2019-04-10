from dealer_blackjack import Dealer_Blackjack
from card import Card

class Dealer_Blackjack_4(Dealer_Blackjack):

	def __init__(self):
		super().__init__()
		self.difficulty = 4

	def get_if_draw(self, deckPile: [Card]) -> bool:
		succNum = 0
		failNum = 0
		for card in deckPile:
			self.cards_on_hand.append(card)
			if (self.get_score() > 21):
				failNum += 1
			else:
				succNum += 1
			self.cards_on_hand.remove(card)
		if (succNum >= failNum):
			return True
		else:
			return False

	def set_init(self):
		self.difficulty = 4
