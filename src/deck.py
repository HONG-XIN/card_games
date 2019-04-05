# -*- coding: utf-8 -*-


from card import Card
from random import shuffle

class Deck:
	def __init__(self, numOfDeck):
		self.numOfDeck = numOfDeck
		self.deckPile = []
		self.drawPile = []

	def initialize(self):
		self.deckPile = []
		self.drawPile = []
		for i in range(self.numOfDeck):
			for color in ["spades", "hearts", "clubs", "diamonds"]:
				for number in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]:
					self.deckPile.append(Card(number, color))

	def shuffle(self):
		shuffle(self.deckPile)

	def draw(self):
		# 时间复杂度考虑 (拿最后一张 O(1))
		c = self.deckPile.pop()
		self.drawPile.append(c)
		return c

	def getDeckPile(self):
		return self.deckPile

