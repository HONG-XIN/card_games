from game import *
from player_blackjack import Player_Blackjack
from dealer_blackjack import Dealer_Blackjack
from dealer_blackjack_1 import Dealer_Blackjack_1
from dealer_blackjack_2 import Dealer_Blackjack_2
from dealer_blackjack_3 import Dealer_Blackjack_3
from dealer_blackjack_4 import Dealer_Blackjack_4

class Game_Blackjack(Game):

	def __init__(self):
		super().__init__()
		self.you = Player_Blackjack()
		self.dealer = Dealer_Blackjack()
		self.you_end = False
		self.dealer_end = False

	def get_if_end(self) -> bool:
		return self.you_end and self.dealer_end

	def get_winner(self) -> str:
		you_score = self.you.get_score()
		dealer_score = self.dealer.get_score()
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

	def set_dealer_difficulty(self, num: int) -> None:
		if num == 1:
			self.dealer.__class__ = Dealer_Blackjack_1
		elif num == 2:
			self.dealer.__class__ = Dealer_Blackjack_2
		elif num == 3:
			self.dealer.__class__ = Dealer_Blackjack_3
		elif num == 4:
			self.dealer.__class__ = Dealer_Blackjack_4
		self.dealer.set_init()

	def start(self) -> None:
		self._clear_variables()
		self._init_deck()

	def stop(self) -> None:
		self.you_end = True
		self._dealer_draws_to_end()

	def deck_draw_one(self) -> None:
		self.you.draws(self.deck.draw())
		if self.you.get_able_continue():
			if not self.dealer_end:
				if self.dealer.__class__ == Dealer_Blackjack_4:
					whether_draw = self.dealer.get_if_draw(self.deck.get_deck_pile())
				else:
					whether_draw = self.dealer.get_if_draw()
				if whether_draw:
					self.dealer.draws(self.deck.draw())
					if not self.dealer.get_able_continue():
						self.dealer_end = True
				else:
					self.dealer_end = True
			else:
				self.you_end = True
		else:
			self.you_end = True
			self._dealer_draws_to_end()

######################### private methods #########################

	def _clear_variables(self):
		super()._clear_variables()
		self.you = Player_Blackjack()
		self.dealer = Dealer_Blackjack()
		self.you_end = False
		self.dealer_end = False

	def _init_deck(self):
		self.deck = Deck(1)
		self.deck.initialize()
		self._deck_shuffle()

		# Everyone draws 1 card
		self.you.draws(self.deck.draw())
		if not self.you.get_able_continue():
			self.you_end = True

		self.dealer.draws(self.deck.draw())
		if not self.dealer.get_able_continue():
			self.dealer_end = True

	def _dealer_draws_to_end(self):
		while not self.dealer_end:
			if self.dealer.__class__ == Dealer_Blackjack_4:
				whether_draw = self.dealer.get_if_draw(self.deck.get_deck_pile())
			else:
				whether_draw = self.dealer.get_if_draw()
			if whether_draw:
				self.dealer.draws(self.deck.draw())
				if not self.dealer.get_able_continue():
					self.dealer_end = True
			else:
				self.dealer_end = True
