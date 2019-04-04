from game import Game

class Panel:
	def __init__(self):
		self.game = None

	def twentyOne_menu(self):
		print("#############################################################")
		print("[21-points] Commands:                                     <<<")
		print(">>> 1. Human vs Human                                     <<<")
		print(">>> 2. Human vs Dealer (difficulty=1)                     <<<")
		print(">>> 3. Human vs Dealer (difficulty=2)                     <<<")
		print(">>> 4. Human vs Dealer (difficulty=3)                     <<<")
		print(">>> 5. Human vs Dealer (difficulty=4)                     <<<")
		print(">>> show. Display current players                         <<<")
		print(">>> clear. Clear all players                              <<<")
		print(">>> add [name]. Add one player                            <<<")
		print(">>> dealer [difficulty in [1,4]]. Add one dealer          <<<")
		print(">>> start. Start the game                                 <<<")
		print(">>> up                                                    <<<")
		print("#############################################################")
		g = Game(self.game)
		while True:
			command = raw_input('$ ')
			if (command == "up"):
				self.main_menu()
				break
			elif (command == "1"):
				g.addPlayer('A')
				g.addPlayer('B')
				g.play()
				self.main_menu()
				break
			elif (command == "2"):
				g.addPlayer('A')
				g.addPlayer('Dealer', 1)
				g.play()
				self.main_menu()
				break
			elif (command == "3"):
				g.addPlayer('A')
				g.addPlayer('Dealer', 2)
				g.play()
				self.main_menu()
				break
			elif (command == "4"):
				g.addPlayer('A')
				g.addPlayer('Dealer', 3)
				g.play()
				self.main_menu()
				break
			elif (command == "5"):
				g.addPlayer('A')
				g.addPlayer('Dealer', 4)
				g.play()
				self.main_menu()
				break
			elif (command == "show"):
				g.printPlayers()
			elif (command == "clear"):
				g.clearPlayers()
			elif (command.split(' ')[0] == "add"):
				g.addPlayer(command.split(' ')[1])
			elif (command.split(' ')[0] == "dealer"):
				if command.split(' ')[1] not in ['1', '2', '3', '4']:
					print("Error: difficulty not valid")
				else:
					g.addPlayer('Dealer', int(command.split(' ')[1]))
			elif (command == "start"):
				if (g.getPlayersNum() < 2):
					print("Error: players number not enough")
				else:
					g.play()
					self.main_menu()
					break
			else:
				print("Error input")

	def main_menu(self):
		print("###############################")
		print(">>> 1. 21-points            <<<")
		print(">>> up                      <<<")
		print("###############################")
		while True:
			command = raw_input('$ ')
			if (command == "up"):
				self.run()
				break
			elif (command == "1"):
				self.game = "21-points"
				self.twentyOne_menu()
				break
			else:
				print("Error input")

	def run(self):
		print("##################")
		print(">>> play       <<<")
		print(">>> exit       <<<")
		print("##################")
		while True:
			command = raw_input('$ ')
			if (command == "exit"):
				break
			elif (command == "play"):
				self.main_menu()
				break
			else:
				print("Error input")
