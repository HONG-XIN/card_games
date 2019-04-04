import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QRadialGradient
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class App(QWidget):

	def __init__(self):
		super().__init__()
		self.title = "Card Games"
		self.left = 10
		self.top = 10
		self.width = 600
		self.height = 900
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		# Set window background color
		p = QPalette()
		gradient = QRadialGradient(300, 450, 500)
		gradient.setColorAt(0.0, QColor(0, 108, 31))
		gradient.setColorAt(1.0, QColor(0, 64, 18))
		p.setBrush(QPalette.Window, QBrush(gradient))
		self.setPalette(p)

		# Set main menu title
		pic = QLabel(self)
		pic.setGeometry(0, 200, 600, 100)
		pic.setAlignment(Qt.AlignCenter)
		pic.setPixmap(QPixmap("../res/images/menu_title.png"))

		# Exit button
		exit_button = QPushButton('EXIT', self)
		exit_button.clicked.connect(self.close)
		exit_button.resize(100, 36)
		exit_button.move(410, 780)
		
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
