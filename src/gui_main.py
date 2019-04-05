import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QRadialGradient
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

StyleSheet = '''
QPushButton {
	min-width: 200px;
	max-width: 200px;
	min-height: 36px;
	max-height: 36px;	
}

QPushButton#level1 {
	min-width: 100px;
	max-width: 100px;
	min-height: 36px;
	max-height: 36px;	
}


QPushButton:hover {
	background-color: #ffffff;
}
'''

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = "Card Games"
		self.left = 10
		self.top = 10
		self.width = 600
		self.height = 900
		self.main_menu_widgets = []
		self.blackjack_menu_widgets = []
		self.blackjack_game_widgets = {
			"stable": [],
			"option": [],
			"cards1": [],
			"cards2": []
		}

		self._initUI()

	def _initUI(self):
		# Set window title and background color
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		# Set window background color
		p = QPalette()
		gradient = QRadialGradient(300, 450, 500)
		gradient.setColorAt(0.0, QColor(0, 108, 31))
		gradient.setColorAt(1.0, QColor(0, 64, 18))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)

		# Initialize main menu widgets
		self._init_main_menu_widgets()
		self._init_blackjack_menu_widgets()
		self._init_blackjack_game_widgets()

		# self._display_main_menu()
		# self._display_blackjack_menu()
		self._display_blackjack_game()

		self.show()

	def _init_main_menu_widgets(self):
		# Set main menu title
		pic = QLabel(self)
		pic.setGeometry(0, 200, 600, 100)
		pic.setAlignment(Qt.AlignCenter)
		pic.setPixmap(QPixmap("../res/images/menu_title.png"))
		
		# Set menu left-bottom decoration
		dec = QLabel(self)
		dec.setGeometry(20, 520, 600, 500)
		dec.setPixmap(QPixmap("../res/images/menu_decoration.png"))	

		# Set Blackjack game button
		blackjack_button = QPushButton('Blackjack', self)
		blackjack_button.move(200, 400)
		blackjack_button.clicked.connect(self._display_blackjack_menu)
		
		# Set Texas Hold'em game button
		texas_holdem_button = QPushButton('Texas Hold\'em', self)
		texas_holdem_button.move(200, 450)
		# texas_holdem_button.clicked.connect()

		# Exit button
		exit_button = QPushButton('EXIT', self)
		exit_button.setObjectName('level1')
		exit_button.clicked.connect(self.close)
		exit_button.move(410, 780)

		# Store these widgets to self variable
		self.main_menu_widgets.append(pic)
		self.main_menu_widgets.append(dec)
		self.main_menu_widgets.append(blackjack_button)
		self.main_menu_widgets.append(texas_holdem_button)
		self.main_menu_widgets.append(exit_button)

	def _init_blackjack_menu_widgets(self):
		# Set Blackjack icon image
		pic = QLabel(self)
		pic.setGeometry(0, 200, 600, 100)
		pic.setAlignment(Qt.AlignCenter)
		pic.setPixmap(QPixmap("../res/images/blackjack_icon.png"))

		# Set AI(1) button
		ai1_button = QPushButton("Simple AI", self)
		ai1_button.move(200, 400)

		# Set AI(2) button
		ai2_button = QPushButton("Medium AI", self)
		ai2_button.move(200, 450)

		# Set AI(3) button
		ai3_button = QPushButton("Hard AI", self)
		ai3_button.move(200, 500)

		# Set AI(4) button
		ai4_button = QPushButton("Hard+ AI", self)
		ai4_button.move(200, 550)

		# Back button
		back_button = QPushButton("BACK", self)
		back_button.setObjectName('level1')
		back_button.clicked.connect(self._display_main_menu)
		back_button.move(90, 780)

		# Exit button
		exit_button = QPushButton('EXIT', self)
		exit_button.setObjectName('level1')
		exit_button.clicked.connect(self.close)
		exit_button.move(410, 780)

		# Store these variables
		self.blackjack_menu_widgets.append(pic)
		self.blackjack_menu_widgets.append(ai1_button)
		self.blackjack_menu_widgets.append(ai2_button)
		self.blackjack_menu_widgets.append(ai3_button)
		self.blackjack_menu_widgets.append(ai4_button)
		self.blackjack_menu_widgets.append(back_button)
		self.blackjack_menu_widgets.append(exit_button)

	def _init_blackjack_game_widgets(self):
		# Dealer icon
		dealer_icon = QLabel(self)
		dealer_icon.setGeometry(0, 50, 600, 100)
		dealer_icon.setAlignment(Qt.AlignCenter)
		dealer_icon.setPixmap(QPixmap("../res/images/dealer_icon.png"))

		# You icon
		you_icon = QLabel(self)
		you_icon.setGeometry(0, 600, 600, 100)
		you_icon.setAlignment(Qt.AlignCenter)
		you_icon.setPixmap(QPixmap("../res/images/you_icon.png"))

		# Back button
		back_button = QPushButton("BACK", self)
		back_button.setObjectName('level1')
		back_button.clicked.connect(self._display_blackjack_menu)
		back_button.move(90, 780)

		# Draw button
		draw_button = QPushButton('DRAW', self)
		draw_button.setObjectName('level1')
		# draw_button.clicked.connect(self.close)
		draw_button.move(410, 730)

		# Stop button
		stop_button = QPushButton('STOP', self)
		stop_button.setObjectName('level1')
		# stop_button.clicked.connect(self.close)
		stop_button.move(410, 780)

		# Store these variables
		self.blackjack_game_widgets["stable"].append(dealer_icon)
		self.blackjack_game_widgets["stable"].append(you_icon)
		self.blackjack_game_widgets["stable"].append(back_button)
		self.blackjack_game_widgets["option"].append(draw_button)
		self.blackjack_game_widgets["option"].append(stop_button)

	def _display_main_menu(self):
		self._hide_blackjack_menu()
		self._hide_blackjack_game()
		for widget in self.main_menu_widgets:
			widget.show()

	def _display_blackjack_menu(self):
		self._hide_main_menu()
		self._hide_blackjack_game()
		for widget in self.blackjack_menu_widgets:
			widget.show()

	def _display_blackjack_game(self):
		self._hide_main_menu()
		self._hide_blackjack_menu()
		for key in self.blackjack_game_widgets.keys():
			for widget in self.blackjack_game_widgets[key]:
				widget.show()

	def _hide_main_menu(self):
		for widget in self.main_menu_widgets:
			widget.hide()

	def _hide_blackjack_menu(self):
		for widget in self.blackjack_menu_widgets:
			widget.hide()

	def _hide_blackjack_game(self):
		for key in self.blackjack_game_widgets.keys():
			for widget in self.blackjack_game_widgets[key]:
				widget.hide()

def main():
	app = QApplication(sys.argv)
	app.setStyleSheet(StyleSheet)
	ex = App()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
