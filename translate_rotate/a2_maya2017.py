# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

try:
	from PySide import QtCore
	from PySide import QtWidgets
except:
	from PySide2 import QtCore
	from PySide2 import QtGui
	from PySide2 import QtWidgets

import maya.cmds as cmds

class Widget(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)

		self.default = dict()

		# DIAL --------------------------------------------
		# Dial x
		self.nDialx = QtWidgets.QDial()
		self.nDialx.setNotchesVisible(True)
		self.nDialx.setMinimum(0)
		self.nDialx.setMaximum(360)
		self.nDialx.setValue(0) # default start from the beginning
		# Dial y
		self.nDialy = QtWidgets.QDial()
		self.nDialy.setNotchesVisible(True)
		self.nDialy.setMinimum(0)
		self.nDialy.setMaximum(360)
		self.nDialy.setValue(0) # default start from the beginning
		# Dial z
		self.nDialz = QtWidgets.QDial()
		self.nDialz.setNotchesVisible(True)
		self.nDialz.setMinimum(0)
		self.nDialz.setMaximum(360)
		self.nDialz.setValue(0) # default start from the beginning

		# SLIDE -------------------------------------------
		# Slide Horizontal X
		self.nSlidex = QtWidgets.QSlider(QtCore.Qt.Horizontal) 
		self.nSlidex.setMinimum(-20)
		self.nSlidex.setMaximum(20)
		self.nSlidex.setValue(0)

		# Slide Vertical Y
		self.nSlidey = QtWidgets.QSlider(QtCore.Qt.Vertical)
		self.nSlidey.setMinimum(-20)
		self.nSlidey.setMaximum(20)
		self.nSlidey.setValue(0)

		# Slide Horizontal Z
		self.nSlidez = QtWidgets.QSlider(QtCore.Qt.Horizontal) 
		self.nSlidez.setMinimum(-20)
		self.nSlidez.setMaximum(20)
		self.nSlidez.setValue(0)

		# Reset button
		self.resetBtn = QtWidgets.QPushButton('Reset')
		# Close button
		self.closeBtn = QtWidgets.QPushButton('Close')

		self.nGridLayout = QtWidgets.QGridLayout()

		self.nGridLayout.addWidget(self.nDialx, 1, 0)
		self.nGridLayout.addWidget(self.nDialy, 1, 1)
		self.nGridLayout.addWidget(self.nDialz, 1, 2)

		self.nGridLayout.addWidget(self.nSlidex, 2, 0)
		self.nGridLayout.addWidget(self.nSlidey, 2, 1)
		self.nGridLayout.addWidget(self.nSlidez, 2, 2)

		self.nGridLayout.addWidget(self.resetBtn, 3, 1)
		self.nGridLayout.addWidget(self.closeBtn, 3, 2)
		self.setLayout(self.nGridLayout)
		self.setWindowTitle('Soovii - Bluk loader')

		# Create connection
		self.connect(self.nDialx, QtCore.SIGNAL("valueChanged(int)"), self.nRo)
		self.connect(self.nDialy, QtCore.SIGNAL("valueChanged(int)"), self.nRo)
		self.connect(self.nDialz, QtCore.SIGNAL("valueChanged(int)"), self.nRo)

		self.connect(self.nSlidex, QtCore.SIGNAL("valueChanged(int)"), self.nRt)
		self.connect(self.nSlidey, QtCore.SIGNAL("valueChanged(int)"), self.nRt)
		self.connect(self.nSlidez, QtCore.SIGNAL("valueChanged(int)"), self.nRt)

		self.connect(self.resetBtn, QtCore.SIGNAL("clicked()"), self.nReset)
		self.connect(self.closeBtn, QtCore.SIGNAL("clicked()"), self.close)

	# Rotation
	def nRo(self):
		sels = cmds.ls(sl=True)
		if len(self.default) == 0:
			for sel in sels:
				xo, yo, zo = cmds.xform(sel, q=True, ws=True, ro=True)
				xt, yt, zt = cmds.xform(sel, q=True, ws=True, rt=True)
				self.default[sel] = [xo, yo, zo, xt, yt, zt]

		for sel in sels:
			x, y, z = cmds.xform(sel, q=True, ws=True, ro=True)
			x = self.nDialx.value() if self.nDialx.value() else x
			y = self.nDialy.value() if self.nDialy.value() else y
			z = self.nDialz.value() if self.nDialz.value() else z
			cmds.xform(sel, ws=True, ro=[x, y, z])

	# Rotation Translation
	def nRt(self):
		sels = cmds.ls(sl=True)
		if len(self.default) == 0:
			for sel in sels:
				xo, yo, zo = cmds.xform(sel, q=True, ws=True, ro=True)
				xt, yt, zt = cmds.xform(sel, q=True, ws=True, rt=True)
				self.default[sel] = [xo, yo, zo, xt, yt, zt]

		for sel in sels:
			x, y, z = cmds.xform(sel, q=True, ws=True, rt=True)
			x = self.nSlidex.value() if self.nSlidex.value() else x
			y = self.nSlidey.value() if self.nSlidey.value() else y
			z = self.nSlidez.value() if self.nSlidez.value() else z
			cmds.xform(sel, ws=True, rt=[x, y, z])

	def nReset(self):
		if len(self.default) == 0:
			return
		for k, v in self.default.items():
			xo, yo, zo, xt, yt, zt = v
			cmds.xform(k, ws=True, ro=[xo, yo, zo], rt=[xt, yt, zt])
		self.default = dict()


if __name__ == '__main__':
	w = Widget()
	w.show()
