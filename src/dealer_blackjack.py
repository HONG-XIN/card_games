from dealer import Dealer
from rule_blackjack import Rule_Blackjack

class Dealer_Blackjack(Dealer):

	def __init__(self):
		super().__init__()
		self.game_name = "Blackjack"
		self.rule = Rule_Blackjack()

	def get_score(self) -> int: # Get current score
		return self.rule.get_score(self.cards_on_hand)

	def get_able_continue(self) -> bool:
		return self.rule.get_able_continue(self.cards_on_hand)
