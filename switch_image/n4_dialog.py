# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

try:
	from PySide import QtCore
	from PySide import QtGui
except ImportError:
	from PySide2 import QtCore
	from PySide2 import QtGui
	from PySide2 import QtWidgets

# import maya.cmds as cmds

class Dialog(QtGui.QDialog):
	def __init__(self):
		super(Dialog, self).__init__()

		self.createOptionsGroupBox()
		self.createButtonBox()

		mainLayout = QtGui.QGridLayout()
		mainLayout.addWidget(self.optionsGroupBox, 0, 0)
		mainLayout.addWidget(self.buttonBox, 1, 0)
		mainLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)

		self.mainLayout = mainLayout
		self.setLayout(self.mainLayout)
		self.setWindowTitle("Soovii - Reverse Node")

	def createOptionsGroupBox(self):

		self.optionsGroupBox = QtGui.QGroupBox("Nodes")
		NodeLabel = QtGui.QLabel("Select a Node:")
		NodeCombo = QtGui.QComboBox()
		NodeCombo.addItem("Node 1")
		NodeCombo.addItem("Node 2")
		NodeCombo.addItem("Node 3")

		self.NodeCombo = NodeCombo

		NodeLayout = QtGui.QGridLayout()
		NodeLayout.addWidget(NodeLabel, 0, 0)
		NodeLayout.addWidget(self.NodeCombo, 0, 1)
		NodeLayout.setColumnStretch(2,1)
		self.optionsGroupBox.setLayout(NodeLayout)

	def createButtonBox(self):
		self.buttonBox = QtGui.QDialogButtonBox()
		closeButton = self.buttonBox.addButton(QtGui.QDialogButtonBox.Close)
		reverseButton = self.buttonBox.addButton('Reverse', QtGui.QDialogButtonBox.ActionRole)

		closeButton.clicked.connect(self.close)
		reverseButton.clicked.connect(self.reverseAct)

	def reverseAct(self): pass

if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	dialog = Dialog()
	dialog.exec_()
