class Card:
	def __init__(self, number, color):
		self.number = number
		self.color = color

	def getNumber(self):
		return self.number

	def get_png_file_name(self):
		reply = ""
		if self.number == 'A':
			reply += "ace"
		elif self.number == 'J':
			reply += "jack"
		elif self.number == 'Q':
			reply += "queen"
		elif self.number == 'K':
			reply += "king"
		else:
			reply += str(self.number)
		reply += "_of_"
		reply += self.color + ".png"
		return reply
