# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

try:
	from PySide import QtCore
	from PySide import QtGui
except ImportError:
	from PySide2 import QtCore
	from PySide2 import QtGui
	from PySide2 import QtWidgets

import maya.cmds as cmds

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		self.toggle = True
		self.nLeft, self.nRight = None, None

		self.createActions()
		self.createMenus()		
		self.createDockWindows()
				
		self.setWindowTitle("Soovii - Reverse Node")
		self.resize(500, 400)
		
	def createDockWindows(self):
		self.dockLeft = QtWidgets.QDockWidget('Original', self)
		self.nLeftLabel = QtWidgets.QLabel()
		self.nLeftLabel.setBackgroundRole(QtGui.QPalette.Base)
		self.nLeftLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		self.nLeftLabel.setScaledContents(True)
		self.dockLeft.setBackgroundRole(QtGui.QPalette.Dark)
		self.dockLeft.setWidget(self.nLeftLabel)
		self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dockLeft)
				
		self.dockRight = QtWidgets.QDockWidget('Reverse', self)
		self.nRightLabel = QtWidgets.QLabel()
		self.nRightLabel.setBackgroundRole(QtGui.QPalette.Base)
		self.nRightLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
		self.nRightLabel.setScaledContents(True)
		self.dockRight.setBackgroundRole(QtGui.QPalette.Dark)
		self.dockRight.setWidget(self.nRightLabel)
		self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dockRight)

	def createMenus(self):
		# Menu Run
		self.runMenu = QtWidgets.QMenu("&Run", self)
		self.runMenu.addAction(self.runLoadAct)
		self.runMenu.addAction(self.runSwitchAct)
		self.runMenu.addSeparator()
		self.runMenu.addAction(self.exitAct)

		# Menu Help
		self.helpMenu = QtWidgets.QMenu("&Help", self)
		self.helpMenu.addAction(self.helpHowtoAct)

		# Menubar
		self.menuBar().addMenu(self.runMenu)
		self.menuBar().addMenu(self.helpMenu)

	def createActions(self):
		self.runLoadAct = QtWidgets.QAction("&Load", self, shortcut="Ctrl+L", triggered=self._runLoadAct)
		self.runSwitchAct = QtWidgets.QAction("&Switch", self, shortcut="Ctrl+S", triggered=self._runSwitchAct)
		self.exitAct = QtWidgets.QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)
		self.helpHowtoAct = QtWidgets.QAction("&How to", self, shortcut="Ctrl+H", triggered=self._helpHowtoAct)

	def _runLoadAct(self):
		myCube = cmds.polyCube()



	def _runSwitchAct(self): pass
	def _helpHowtoAct(self): pass


if __name__ == '__main__':
	win = Window()
	win.show()