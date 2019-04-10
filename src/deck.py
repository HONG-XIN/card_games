# -*- coding: utf-8 -*-

from card import Card
from random import shuffle

class Deck:
	def __init__(self, num_of_deck):
		self.num_of_deck = num_of_deck
		self.deck_pile = []
		self.draw_pile = []

	def get_deck_pile(self) -> [Card]:
		return self.deck_pile

	def initialize(self) -> None:
		self.deck_pile = []
		self.draw_pile = []
		for i in range(self.num_of_deck):
			for color in ["spades", "hearts", "clubs", "diamonds"]:
				for number in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]:
					self.deck_pile.append(Card(number, color))

	def shuffle(self) -> None:
		shuffle(self.deck_pile)

	def draw(self) -> Card:
		# 时间复杂度考虑 (拿最后一张 O(1))
		c = self.deck_pile.pop()
		self.draw_pile.append(c)
		return c
