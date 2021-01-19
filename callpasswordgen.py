import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import pyperclip
import passwordgen
import filesave
import Algorithm
import webbrowser
import os.path
from os import path

class FileSave(QDialog):
	def __init__(self):
		super(FileSave, self).__init__()
		self.ui = filesave.Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.saveButton.clicked.connect(self.save)

	def save(self):
		self.accounttype = self.ui.accounttypeLine.text()
		self.webURL = self.ui.websiteURLLine.text()
		self.username = self.ui.usernameLine.text()
		self.password = self.ui.passwordLine.text()
		with open("passman.txt",'a+') as f:
			f.write("type=" + self.accounttype + "\nwebURL=" + self.webURL + "\nusername=" + self.username + "\npassword=" + self.password + '\n')
		f.close()
		self.close()

class MyApp(QMainWindow):
	def __init__(self):
		super(MyApp, self).__init__()
		self.password = ""
		self.ui = passwordgen.Ui_mainWindow()
		self.ui.setupUi(self)
		self.ui.generateButton.clicked.connect(self.generate)
		self.ui.copyButton.clicked.connect(self.copy)
		self.ui.filesaveButton.clicked.connect(self.filesave)
		self.filesave = FileSave()
		self.filesave.ui.saveButton.clicked.connect(self.dialogclose)
		self.ui.tabWidget.setCurrentIndex(0)
		self.ui.comboBox.addItem("Select Type of Account")
		self.ui.comboBox.insertSeparator(1)
		self.ui.tabWidget.currentChanged.connect(self.options)
		self.ui.comboBox.currentTextChanged.connect(self.dispoption)
		self.ui.editaccountButton.clicked.connect(self.editaccount)
		self.ui.openURLButton.clicked.connect(self.openURL)
		self.ui.copyusernameButton.clicked.connect(self.copyusername)
		self.ui.copypasswordButton.clicked.connect(self.copypassword)
		self.ui.statusbar.showMessage("Ready")

		self.show()
	def generate(self):
		self.passwordlength = self.ui.passLine.value()
		self.password = Algorithm.generator(self.passwordlength)
		self.ui.password.setText(self.password)
		self.ui.statusbar.showMessage("New Password Generated")

	def copy(self):
		pyperclip.copy(self.ui.password.text())
		self.ui.statusbar.showMessage("Copied to Clipboard")

	def filesave(self):
		self.filesave.ui.passwordLine.setText(self.password)
		self.filesave.show()

	def dialogclose(self):
		self.ui.statusbar.showMessage("Saved to File")
		
	def options(self):
		if path.exists("passman.txt"):
			self.accounts = open("passman.txt",'r')
			self.lines = self.accounts.readlines()
			self.fields = []
			x = []
			for line in self.lines:
				x = line.split("=")
				self.fields.append(x[1][:-1])
			for i in range(0,len(self.fields),4):
				if self.ui.comboBox.findText(self.fields[i]) == -1:
					self.ui.comboBox.addItem(self.fields[i])

	def dispoption(self):
		if path.exists("passman.txt"):
			if self.ui.comboBox.currentText() in self.fields:
				self.ui.websiteURLLine.setText(self.fields[self.fields.index(self.ui.comboBox.currentText())+1])
				self.ui.usernameLine.setText(self.fields[self.fields.index(self.ui.comboBox.currentText())+2])
				self.ui.passwordLine.setText(self.fields[self.fields.index(self.ui.comboBox.currentText())+3])
			else:
				self.ui.websiteURLLine.setText("")
				self.ui.usernameLine.setText("")
				self.ui.passwordLine.setText("")

	def editaccount(self):
		self.filesave.ui.accounttypeLine.setText(self.ui.comboBox.currentText())
		self.filesave.ui.websiteURLLine.setText(self.ui.websiteURLLine.text())
		self.filesave.ui.usernameLine.setText(self.ui.usernameLine.text())
		self.filesave.ui.passwordLine.setText(self.ui.passwordLine.text())
		self.filesave.show()

	def openURL(self):
		webbrowser.open("http://" + self.ui.websiteURLLine.text())

	def copyusername(self):
		pyperclip.copy(self.ui.usernameLine.text())
		self.ui.statusbar.showMessage("Copied to Clipboard")

	def copypassword(self):
		pyperclip.copy(self.ui.passwordLine.text())
		self.ui.statusbar.showMessage("Copied to Clipboard")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MyApp()
	w.show()
	sys.exit(app.exec_())
