import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyperclip
import passwordgen
import Algorithm

class MyApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = passwordgen.Ui_mainWindow()
		self.ui.setupUi(self)
		self.ui.generateButton.clicked.connect(self.generate)
		self.ui.copyButton.clicked.connect(self.copy)
		self.ui.statusbar.showMessage("Ready")

		self.show()
	def generate(self):
		if self.ui.passLine.text() == "":
			self.passwordlength = 0
		else:
			self.passwordlength = self.ui.passLine.text()
		self.password = Algorithm.generator(self.passwordlength)
		self.ui.password.setText(self.password)
		self.ui.statusbar.showMessage("New Password Generated")

	def copy(self):
		pyperclip.copy(self.ui.password.text())
		self.ui.statusbar.showMessage("Copied to Clipboard")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MyApp()
	w.show()
	sys.exit(app.exec_())
