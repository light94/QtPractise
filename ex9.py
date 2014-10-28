import sys
from PyQt4 import QtGui

class Example(QtGui.QMainWindow):

	def __init__(self):
		super(Example,self).__init__()

		self.initUI()

	def initUI(self):

		textEdit = QtGui.QTextEdit()
		self.setCentralWidget(textEdit)

		exitAction = QtGui.QAction(QtGui.QIcon('quit.jpg'),'Exit',self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(self.close)

		self.statusBar()

		menubar = self.menuBar()
		filemenu = menubar.addMenu('&File')
		filemenu.addAction(exitAction)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAction)

		self.setGeometry(300,300,250,250)
		self.setWindowTitle('Main Wnidow')
		self.show()

def main():

	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()