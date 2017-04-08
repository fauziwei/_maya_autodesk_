# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

try:
	from PySide import QtCore
	from PySide import QtGui
except ImportError:
	from PySide2 import QtCore
	from PySide2 import QtGui


class Window(QtGui.QMainWindow):
# class Window(QtGui.QLabel):
	def __init__(self):
		super(Window, self).__init__()

		self.imLabel = QtGui.QLabel()
		self.imLabel.setBackgroundRole(QtGui.QPalette.Base)
		self.imLabel.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
		self.imLabel.setScaledContents(True)

		self.scrollArea = QtGui.QScrollArea()
		self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
		self.scrollArea.setWidget(self.imLabel)
		self.setCentralWidget(self.scrollArea)

		self.imLeft, self.imRight = None, None

		self.createActions()
		self.createMenus()

		self.setWindowTitle("Soovii - Switch Image")
		self.resize(500, 400)

	def createMenus(self):
		# Menu Import
		self.importMenu = QtGui.QMenu("&Import", self)
		self.importMenu.addAction(self.importLeftAct)
		self.importMenu.addAction(self.importRightAct)
		self.importMenu.addSeparator()
		self.importMenu.addAction(self.exitAct)

		# Menu Run
		self.runMenu = QtGui.QMenu("&Run", self)
		self.runMenu.addAction(self.runSwitchAct)

		# Menu Help
		self.helpMenu = QtGui.QMenu("&Help", self)
		self.helpMenu.addAction(self.helpHowtoAct)

		# Menubar
		self.menuBar().addMenu(self.importMenu)
		self.menuBar().addMenu(self.runMenu)
		self.menuBar().addMenu(self.helpMenu)

	def createActions(self):
		self.importLeftAct = QtGui.QAction("Image &left...", self, shortcut="Ctrl+L", triggered=self._importLeftAct)
		self.importRightAct = QtGui.QAction("Image &right...", self, shortcut="Ctrl+R", triggered=self._importRightAct)
		self.exitAct =QtGui.QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)

		self.runSwitchAct = QtGui.QAction("&Switch", self, shortcut="Ctrl+S", triggered=self._runSwitchAct)

		self.helpHowtoAct = QtGui.QAction("&How to", self, shortcut="Ctrl+H", triggered=self._helpHowtoAct)

	def _importLeftAct(self):
		im, _ = QtGui.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath())
		if im:
			self.imLeft = QtGui.QImage(im)
			if self.imLeft.isNull():
				QtGui.QMessageBox.information(self, "Soovii - Switch Image", "Unable to load %s." % im)
				return
			self.imLabel.setPixmap(QtGui.QPixmap.fromImage(self.imLeft))
			self.imLabel.adjustSize()
			self.scrollArea.setWidgetResizable(True)
			print 'self.imLeft:  %s' % self.imLeft
			print 'self.imRight: %s' % self.imRight

	def _importRightAct(self):
		im, _ = QtGui.QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.currentPath())
		if im:
			self.imRight = QtGui.QImage(im)
			if self.imRight.isNull():
				QtGui.QMessageBox.information(self, "Soovii - Switch Image", "Unable to load %s." % im)
				return
			self.imLabel.setPixmap(QtGui.QPixmap.fromImage(self.imRight))
			self.imLabel.adjustSize()
			self.scrollArea.setWidgetResizable(True)
			print 'self.imLeft:  %s' % self.imLeft
			print 'self.imRight: %s' % self.imRight


	def _runSwitchAct(self): pass

	def _helpHowtoAct(self):
		QtGui.QMessageBox.about(self, "Soovii - Switch Image",
			"<p><b>Switch</b> image left and right</p>")



if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	win = Window()
	win.show()
	sys.exit(app.exec_())
