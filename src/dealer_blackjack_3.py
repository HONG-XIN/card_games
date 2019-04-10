from dealer_blackjack import Dealer_Blackjack

class Dealer_Blackjack_3(Dealer_Blackjack):

	def __init__(self):
		super().__init__()
		self.difficulty = 3

	def get_if_draw(self):
		mind = 0
		for card in self.cards_on_hand:
			if (card.getNumber() in ['A', 2, 3, 4, 5]):
				mind += 1
			elif (card.getNumber() in [9, 10, 'J', 'Q', 'K']):
				mind -= 1
		score = self.get_score()
		if (score <= 11):
			return True
		elif (score >= 20):
			return False
		elif (mind + score > 17):
			return False
		else:
			return True

	def set_init(self):
		self.difficulty = 3

# [1, 5] +1
# [9, K] -1
# ___| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21
# -3 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F
# -2 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F
# -1 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F
#  0 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F
#  1 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F
#  2 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F
#  3 | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F | F
#  4 | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F | F | F
#  5 | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F | F | F | F
# mind  >= -2