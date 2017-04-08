# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

import os
try:
	from PySide import QtCore
	from PySide import QtGui
except ImportError:
	from PySide2 import QtCore
	from PySide2 import QtGui
	from PySide2 import QtWidgets

# basedir = os.path.abspath(os.path.dirname(__file__))

class Window(QtWidgets.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()

		self.toggle = True
		self.imLeft, self.imRight = None, None

		self.currentOpenPath = 'C:/Work/Maya/switch_image/'
		# self.currentOpenPath = QtCore.QDir.currentPath()

		self.createActions()
		self.createMenus()
		self.createDockWindows()

		self.setWindowTitle("Soovii - Switch Image")
		self.resize(500, 400)
		iconPath = 'C:\Work\Displacement Map PIL\ico\del_ico_us.ico'
		self.setWindowIcon(QtGui.QIcon(iconPath))

	def createMenus(self):
		# Menu Import
		self.importMenu = QtWidgets.QMenu("&Import", self)
		self.importMenu.addAction(self.importLeftAct)
		self.importMenu.addAction(self.importRightAct)
		self.importMenu.addSeparator()
		self.importMenu.addAction(self.exitAct)

		# Menu Run
		self.runMenu = QtWidgets.QMenu("&Run", self)
		self.runMenu.addAction(self.runSwitchAct)

		# Menu Help
		self.helpMenu = QtWidgets.QMenu("&Help", self)
		self.helpMenu.addAction(self.helpHowtoAct)

		# Menubar
		self.menuBar().addMenu(self.importMenu)
		self.menuBar().addMenu(self.runMenu)
		self.menuBar().addMenu(self.helpMenu)

	def createActions(self):
		self.importLeftAct = QtWidgets.QAction("Image &left...", self, shortcut="Ctrl+L", triggered=self._importLeftAct)
		self.importRightAct = QtWidgets.QAction("Image &right...", self, shortcut="Ctrl+R", triggered=self._importRightAct)
		self.exitAct = QtWidgets.QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)

		self.runSwitchAct = QtWidgets.QAction("&Switch", self, shortcut="Ctrl+S", triggered=self._runSwitchAct)

		self.helpHowtoAct = QtWidgets.QAction("&How to", self, shortcut="Ctrl+H", triggered=self._helpHowtoAct)

	def _importLeftAct(self):
		im, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", self.currentOpenPath)
		if im:
			self.imLeft = QtGui.QImage(im)
			if self.imLeft.isNull():
				QtGui.QMessageBox.information(self, "Soovii - Switch Image", "Unable to load %s." % im)
				return
			self.imLeftLabel.setPixmap(QtGui.QPixmap.fromImage(self.imLeft))
			self.imLeftLabel.adjustSize()

	def _importRightAct(self):
		im, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", self.currentOpenPath)
		if im:
			self.imRight = QtGui.QImage(im)
			if self.imRight.isNull():
				QtGui.QMessageBox.information(self, "Soovii - Switch Image", "Unable to load %s." % im)
				return
			self.imRightLabel.setPixmap(QtGui.QPixmap.fromImage(self.imRight))
			self.imRightLabel.adjustSize()

	def _runSwitchAct(self):
		if self.toggle:
			self.imLeftLabel.setPixmap(QtGui.QPixmap.fromImage(self.imRight))
			self.imLeftLabel.adjustSize()

			self.imRightLabel.setPixmap(QtGui.QPixmap.fromImage(self.imLeft))
			self.imRightLabel.adjustSize()
		else:
			self.imLeftLabel.setPixmap(QtGui.QPixmap.fromImage(self.imLeft))
			self.imLeftLabel.adjustSize()

			self.imRightLabel.setPixmap(QtGui.QPixmap.fromImage(self.imRight))
			self.imRightLabel.adjustSize()

		self.toggle = False if self.toggle else True

	def _helpHowtoAct(self): pass

	def createDockWindows(self):
		self.dockLeft = QtWidgets.QDockWidget('Left image', self)
		#dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
		self.imLeftLabel = QtWidgets.QLabel()
		self.imLeftLabel.setBackgroundRole(QtGui.QPalette.Base)
		self.imLeftLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		self.imLeftLabel.setScaledContents(True)
		self.dockLeft.setBackgroundRole(QtGui.QPalette.Dark)
		self.dockLeft.setWidget(self.imLeftLabel)
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockLeft)


		self.dockRight = QtWidgets.QDockWidget('Right image', self)
		self.imRightLabel = QtWidgets.QLabel()
		self.imRightLabel.setBackgroundRole(QtGui.QPalette.Base)
		self.imRightLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		self.imRightLabel.setScaledContents(True)
		self.dockRight.setBackgroundRole(QtGui.QPalette.Dark)
		self.dockRight.setWidget(self.imRightLabel)
		self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockRight)

if __name__ == '__main__':
	win = Window()
	win.show()
