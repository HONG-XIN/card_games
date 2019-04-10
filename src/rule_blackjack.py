# Sub-class: rule for Blackjack game

from rule import Rule
from card import Card

class Rule_Blackjack(Rule):

	def __init__(self):
		super().__init__()
		self.game_name = "Blackjack"

	def get_game_name(self) -> str:
		return self.game_name

	def get_score(self, cards: [Card]) -> int:
		if len(cards) == 0:
			return 0
		scores = [0]
		for card in cards:
			prevs = scores
			scores = []
			number = card.getNumber()
			for prev in prevs:
				if number == 'A':
					scores.append(prev+1)
					scores.append(prev+11)
				elif number in ['J', 'Q', 'K']:
					scores.append(prev+10)
				else:
					scores.append(prev+number)
		maxInt = 0 # <= 21
		minInt = 999 # > 21
		for score in scores:
			if score <= 21 and score > maxInt:
				maxInt = score
			elif score > 21 and score < minInt:
				minInt = score
		return maxInt if maxInt > 0 else minInt

	def get_able_continue(self, cards: [Card]) -> bool:
		score = self.get_score(cards)
		return True if score <= 21 else False
