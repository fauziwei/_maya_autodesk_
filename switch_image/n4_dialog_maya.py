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

class Dialog(QtWidgets.QDialog):
	def __init__(self):
		super(Dialog, self).__init__()

		self.selectedNode = 0
		self.selections = []

		self.createOptionsGroupBox()
		self.createButtonBox()

		mainLayout = QtWidgets.QGridLayout()
		mainLayout.addWidget(self.optionsGroupBox, 0, 0)
		mainLayout.addWidget(self.buttonBox, 1, 0)
		mainLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)

		self.mainLayout = mainLayout
		self.setLayout(self.mainLayout)
		self.setWindowTitle("Soovii - Reverse Node")

	def createOptionsGroupBox(self):
		self.optionsGroupBox = QtWidgets.QGroupBox("Selection Nodes")
		NodeLabel = QtWidgets.QLabel("Select a node:")
		NodeCombo = QtWidgets.QComboBox()
		self.selections = cmds.ls(sl=True)
		for node in self.selections:
			NodeCombo.addItem(node)
		if len(self.selections) > 0:
			NodeCombo.currentIndexChanged[int].connect(self.nodeSelected)

		self.NodeCombo = NodeCombo

		NodeLayout = QtWidgets.QGridLayout()
		NodeLayout.addWidget(NodeLabel, 0, 0)
		NodeLayout.addWidget(self.NodeCombo, 0, 1)
		NodeLayout.setColumnStretch(2,1)
		self.optionsGroupBox.setLayout(NodeLayout)

	def nodeSelected(self, index):
		self.selectedNode = index

	def createButtonBox(self):
		self.buttonBox = QtWidgets.QDialogButtonBox()
		closeButton = self.buttonBox.addButton(QtWidgets.QDialogButtonBox.Close)
		reverseButton = self.buttonBox.addButton('Reverse', QtWidgets.QDialogButtonBox.ActionRole)

		closeButton.clicked.connect(self.close)
		reverseButton.clicked.connect(self.reverseAct)

	def reverseAct(self):
		if len(self.selections) == 0:
			return
		node = self.selections[self.selectedNode]
		if not node:
			return
		x, y, z = cmds.xform(node, q=True, ws=True, ro=True)
		x *= -1.0
		y *= -1.0
		z *= -1.0
		cmds.xform(node, ws=True, ro=[x, y, z])


if __name__ == '__main__':
	dialog = Dialog()
	dialog.show()
