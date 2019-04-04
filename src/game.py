from deck import Deck
from player import Player
from dealer import Dealer

class Game:
	def __init__(self, game_name):
		self.game = game_name
		self.deck = None
		self.players = {}
		self.turn = None
		self.stopFlag = []
		self.existDealer = False

	def getPlayersNum(self):
		return len(self.players.keys())

	def clearPlayers(self):
		self.players = {}
		self.turn = None
		self.stopFlag = []
		self.existDealer = False

	def printPlayers(self):
		print("In-Game Players:")
		count = 1
		for player in self.players.values():
			if (not isinstance(player, Dealer)):
				print(">>> Player {}: {}".format(count, player.getName()))
				count += 1
			else:
				print(">>> Dealer: Difficulty={}".format(player.getDifficulty()))

	def addPlayer(self, name, dealerDifficulty=0):
		if (dealerDifficulty > 4):
			print("Error: dealer difficulty invalid")
		elif (dealerDifficulty == 0):
			if ('Dealer' not in self.stopFlag):
				self.stopFlag.append(name)
				self.players[name] = Player(name)
			else:
				self.stopFlag.remove('Dealer')
				self.stopFlag.append(name)
				self.players[name] = Player(name)
				self.stopFlag.append('Dealer')
		else:
			if ('Dealer' not in self.stopFlag):
				self.stopFlag.append('Dealer')
				dealer = Dealer('Dealer')
				dealer.setDifficulty(dealerDifficulty)
				self.players['Dealer'] = dealer
				self.existDealer = True
			else:
				print("Error: dealer already exist")

	def configure(self):
		self.deck = Deck(1)
		self.deck.initialize()
		self.deck.shuffle()
		# self.players['A'] = Player('A')
		# self.players['B'] = Player('B')
		# self.stopFlag = ['A', 'B']

	def game21Initial(self):
		for p in self.stopFlag:
			self.players[p].add(self.deck.draw())
			self.players[p].add(self.deck.draw())
		self.turn = self.stopFlag[0]

	def nextTurn(self):
		index = self.stopFlag.index(self.turn)+1
		self.turn = self.stopFlag[index%len(self.stopFlag)]

	def stopPlayer(self):
		index = self.stopFlag.index(self.turn)+1
		tmp = self.stopFlag[index%len(self.stopFlag)]
		self.stopFlag.remove(self.turn)
		if (tmp != self.turn):
			self.turn = tmp
		else:
			self.turn = None


	def isGameEnd(self):
		return (len(self.stopFlag) == 0)

	def winner(self, players):
		nominators = []
		for p in players:
			score = self.players[p].getScore()
			print "{} -> Score: {} -> ".format(p, score),
			self.players[p].displayCards()
			if (score <= 21):
				nominators.append((p, score))
		maxss = 0
		winner = None
		for (sp, ss) in nominators:
			if (ss > maxss):
				winner = sp
				maxss = ss
			elif (ss == maxss):
				winner = winner + ' ' + sp
		return winner

	def printGameResult(self):
		print("*"*40)
		if (not self.existDealer):
			winners = self.winner(self.players.keys())
			if (winners == None):
				print("Draw: {}".format(self.players.keys()))
			elif (len(winners.split(' ')) == 1):
				print("Winner: {}".format(winners))
			else:
				print("Draw: {}".format(winners))
		else:
			for each_name in self.players.keys():
				if (each_name == 'Dealer'):
					continue
				winners = self.winner([each_name, 'Dealer'])
				if (winners == each_name):
					print("{} wins Dealer".format(each_name))
				elif (winners == 'Dealer'):
					print("{} loses to Dealer".format(each_name))
				else:
					print("{}: Draw with Dealer".format(each_name))
				print("*"*40)


	def play(self):
		if (self.game == "21-points"):
			self.configure()
			self.game21Initial()
			print("##################################")
			print(">>> 1. Draw                    <<<")
			print(">>> 2. Show cards on hand      <<<")
			print(">>> 3. Stop.                   <<<")
			print(">>> 4. Get score               <<<")
			print("##################################")
			previous = None
			line_break = False
			while True:
				if self.isGameEnd():
					break
				if (self.turn != previous) or (line_break):
					print("*"*40)
					print("{}'s turn".format(self.turn))
					print("{}'s cards:".format(self.turn))
					self.players[self.turn].displayCards()
					previous = self.turn
					line_break = False
				if (self.turn == 'Dealer'):
					# print("Dealer's difficulty = {}".format(self.players['Dealer'].getDifficulty()))
					if (self.players['Dealer'].ifDraw(16, self.deck.getDeckPile())):
						print("Dealer draws a new card")
						self.players['Dealer'].add(self.deck.draw())
						self.players['Dealer'].displayCards()
						line_break = True
						if (not self.players['Dealer'].canContinue()):
							self.stopPlayer()
							continue
						else:
							self.nextTurn()
					else:
						print("Dealer stops.")
						self.stopPlayer()
					continue
				command = raw_input("$ ")
				if (command == "1"):
					self.players[self.turn].add(self.deck.draw())
					self.players[self.turn].displayCards()
					line_break = True
				elif (command == "2"):
					self.players[self.turn].displayCards()
					continue
				elif (command == "3"):
					self.stopPlayer()
					continue
				elif (command == "4"):
					print("Score: {}".format(self.players[self.turn].getScore()))
					continue
				else:
					print("Error input")
					continue
				if (not self.players[self.turn].canContinue()):
					self.players[self.turn].displayCards()
					self.stopPlayer()
					continue
				self.nextTurn()
			self.printGameResult()

		else:
			print("Invalid game")
