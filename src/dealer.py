# -*- coding: utf-8 -*-

from player import Player
import random

class Dealer(Player):

	def __init__(self):
		Player.__init__(self)
		self.game_name = None
		self.difficulty = None

	def get_game_name(self) -> str:
		return self.game_name

	def get_difficulty(self) -> int:
		return self.difficulty

	# def set_difficulty(self, number: int) -> None:
	# 	self.difficulty = number

	# def ifDraw(self, number, deckPile, score):
	# 	if (self.difficulty == 1):
	# 		return self.ifDraw1()
	# 	elif (self.difficulty == 2):
	# 		return self.ifDraw2(number, score)
	# 	elif (self.difficulty == 3):
	# 		return self.ifDraw3(score)
	# 	elif (self.difficulty == 4):
	# 		return self.ifDraw4(deckPile)

	# def ifDraw1(self):
	# 	# 50%要 50%不要
	# 	return random.choice([True, False])

	# def ifDraw2(self, number, score):
	# 	# >number不要 | <=number要
	# 	if (score <= number):
	# 		return True
	# 	else:
	# 		return False

	# def ifDraw3(self, score):
	# 	# [1, 5] +1
	# 	# [9, K] -1
	# 	# ___| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21
	# 	# -3 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F
	# 	# -2 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F
	# 	# -1 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F
	# 	#  0 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F
	# 	#  1 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F
	# 	#  2 | T | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F
	# 	#  3 | T | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F | F
	# 	#  4 | T | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F | F | F
	# 	#  5 | T | T | T | T | T | T | T | T | T | T | T | F | F | F | F | F | F | F | F | F | F
	# 	# mind  >= -2
	# 	mind = 0
	# 	for card in self.cardOnHand:
	# 		if (card.getNumber() in ['A', 2, 3, 4, 5]):
	# 			mind += 1
	# 		elif (card.getNumber() in [9, 10, 'J', 'Q', 'K']):
	# 			mind -= 1
	# 	if (score <= 11):
	# 		return True
	# 	elif (score >= 20):
	# 		return False
	# 	elif (mind + score > 17):
	# 		return False
	# 	else:
	# 		return True

	# def ifDraw4(self, deckPile):
	# 	succNum = 0
	# 	failNum = 0
	# 	for card in deckPile:
	# 		self.cardOnHand.append(card)
	# 		if (self.getScore() > 21):
	# 			failNum += 1
	# 		else:
	# 			succNum += 1
	# 		self.cardOnHand.remove(card)
	# 	if (succNum >= failNum):
	# 		return True
	# 	else:
	# 		return False

		

# d = Dealer('dealer')
# print(isinstance(d, Player))

