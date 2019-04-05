from game import *
from dealer import Dealer

class Game_Blackjack(Game):

	def __init__(self):
		super().__init__()
		self.you_end = False
		self.dealer_end = False
		self.dealer_AI = Dealer("Dealer")

	def start(self):
		self._clear_variables()
		self._init_deck()

	def set_dealer_difficulty(self, num: int) -> None:
		self.dealer_AI.setDifficulty(num)

	def if_end(self) -> bool:
		return self.you_end and self.dealer_end

	def get_winner(self) -> str:
		you_score = self._get_score(self.you)
		dealer_score = self._get_score(self.dealer)
		if you_score > 21 and dealer_score > 21:
			return "Dealer"
		if you_score > 21:
			return "Dealer"
		if dealer_score > 21:
			return "You"
		if you_score == dealer_score:
			return "Tie"
		if you_score < dealer_score:
			return "Dealer"
		else:
			return "You"

	def stop(self) -> None:
		self.you_end = True
		self._dealer_draws_to_end()

	def deck_draw_one(self) -> None:
		self.you.append(self.deck.draw())
		if self._able_continue(self.you):
			if not self.dealer_end:
				if self.dealer_AI.ifDraw(16, self.deck.getDeckPile()):
					card = self.deck.draw()
					self.dealer.append(card)
					self.dealer_AI.add(card)
					if not self._able_continue(self.dealer):
						self.dealer_end = True
				else:
					self.dealer_end = True
			else:
				self.you_end = True
		else:
			self.you_end = True
			self._dealer_draws_to_end()

	def _dealer_draws_to_end(self):
		while not self.dealer_end:
			if self.dealer_AI.ifDraw(16, self.deck.getDeckPile()):
				card = self.deck.draw()
				self.dealer.append(card)
				self.dealer_AI.add(card)
				if not self._able_continue(self.dealer):
					self.dealer_end = True
			else:
				self.dealer_end = True

	def _init_deck(self):
		self.deck = Deck(1)
		self.deck.initialize()
		self._deck_shuffle()

		# Everyone draws 1 card
		card = self.deck.draw()
		self.you.append(card)
		if not self._able_continue(self.you):
			self.you_end = True
		card = self.deck.draw()
		self.dealer.append(card)
		self.dealer_AI.add(card)
		if not self._able_continue(self.dealer):
			self.dealer_end = True

	def _clear_variables(self):
		super()._clear_variables()
		self.you_end = False
		self.dealer_end = False
		self.dealer_AI = Dealer("Dealer")

	def _get_score(self, cards: [Card]) -> int:
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

	def _able_continue(self, cards: [Card]) -> bool:
		score = self._get_score(cards)
		return True if score <= 21 else False



