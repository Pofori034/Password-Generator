import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyperclip
import passwordgen

class MyApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = passwordgen.Ui_mainWindow()
		self.ui.setupUi(self)
		self.ui.generateButton.clicked.connect(self.generate)
		self.ui.copyButton.clicked.connect(self.copy)

		self.show()
	def generate(self):
		self.passwordlength = self.ui.passLine.text()
		self.ui.label.setText("")

	def copy(self):
		self.password = self.ui.password.text()
		pyperclip.copy(self.password)
		self.ui.label.setText("Copied!")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MyApp()
	w.show()
	sys.exit(app.exec_())
