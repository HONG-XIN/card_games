from card import Card

class Player:
	def __init__(self, name):
		self.name = name
		self.cardOnHand = []
		self.money = 100

	def getName(self):
		return self.name

	def add(self, c):
		self.cardOnHand.append(c)

	def displayCards(self):
		print([c.getNumber() for c in self.cardOnHand])

	def getScore(self):
		if len(self.cardOnHand) == 0:
			return 0
		scores = [0]
		for c in self.cardOnHand:
			M = scores
			scores = []
			for m in M:
				if (c.getNumber() == 'A'):
					scores.append(m+1)
					scores.append(m+11)
				elif (c.getNumber() in ['J', 'Q', 'K']):
					scores.append(m+10)
				else:
					scores.append(m+c.getNumber())
		minScore = 999
		maxScore = 0
		for s in scores:
			if s <= 21 and s > maxScore:
				maxScore = s
			elif s > 21 and s < minScore:
				minScore = s
		if (maxScore > 0):
			return maxScore
		else:
			return minScore

	def canContinue(self):
		if (self.getScore() <= 21):
			return True
		else:
			return False

