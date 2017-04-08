# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

try:
	from PySide import QtCore
	from PySide import QtGui
except:
	from PySide2 import QtCore
	from PySide2 import QtGui
	from PySide2 import QtWidgets

import maya.cmds as cmds

class Widget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		self.nodes = dict()
		sels = cmds.ls(sl=True)
		for sel in sels:
			xr, yr, zr = cmds.xform(sel, q=True, ws=True, ro=True)
			xt, yt, zt = cmds.xform(sel, q=True, ws=True, t=True)
			self.nodes[sel] = [xr, yr, zr, xt, yt, zt]

		# DIAL --------------------------------------------
		# Dial x
		self.nDialx = QtGui.QDial()
		self.nDialx.setNotchesVisible(True)
		self.nDialx.setMinimum(0)
		self.nDialx.setMaximum(360)
		self.nDialx.setValue(0) # default start from the beginning
		# Dial y
		self.nDialy = QtGui.QDial()
		self.nDialy.setNotchesVisible(True)
		self.nDialy.setMinimum(0)
		self.nDialy.setMaximum(360)
		self.nDialy.setValue(0) # default start from the beginning
		# Dial z
		self.nDialz = QtGui.QDial()
		self.nDialz.setNotchesVisible(True)
		self.nDialz.setMinimum(0)
		self.nDialz.setMaximum(360)
		self.nDialz.setValue(0) # default start from the beginning

		# SLIDE -------------------------------------------
		# Slide Horizontal X
		self.nSlidex = QtGui.QSlider(QtCore.Qt.Horizontal) 
		self.nSlidex.setMinimum(-20)
		self.nSlidex.setMaximum(20)
		self.nSlidex.setValue(0)

		# Slide Vertical Y
		self.nSlidey = QtGui.QSlider(QtCore.Qt.Vertical)
		self.nSlidey.setMinimum(-20)
		self.nSlidey.setMaximum(20)
		self.nSlidey.setValue(0)

		# Slide Horizontal Z
		self.nSlidez = QtGui.QSlider(QtCore.Qt.Horizontal) 
		self.nSlidez.setMinimum(-20)
		self.nSlidez.setMaximum(20)
		self.nSlidez.setValue(0)

		# Reset button
		self.resetBtn = QtGui.QPushButton('Reset')
		# Close button
		self.closeBtn = QtGui.QPushButton('Close')

		self.nGridLayout = QtGui.QGridLayout()

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
		self.connect(self.nDialx, QtCore.SIGNAL("valueChanged(int)"), self.nMove)
		self.connect(self.nDialy, QtCore.SIGNAL("valueChanged(int)"), self.nMove)
		self.connect(self.nDialz, QtCore.SIGNAL("valueChanged(int)"), self.nMove)

		# self.connect(self.nSlidex, QtCore.SIGNAL("valueChanged(int)"), self.nMove)
		# self.connect(self.nSlidey, QtCore.SIGNAL("valueChanged(int)"), self.nMove)
		# self.connect(self.nSlidez, QtCore.SIGNAL("valueChanged(int)"), self.nMove)
		self.connect(self.nSlidex, QtCore.SIGNAL("valueChanged(int)"), self.nTransx)
		self.connect(self.nSlidey, QtCore.SIGNAL("valueChanged(int)"), self.nTransy)
		self.connect(self.nSlidez, QtCore.SIGNAL("valueChanged(int)"), self.nTransz)

		self.connect(self.resetBtn, QtCore.SIGNAL("clicked()"), self.nReset)
		self.connect(self.closeBtn, QtCore.SIGNAL("clicked()"), self.close)

	# nMove
	def nMove(self):
		if len(self.nodes) == 0:
			sels = cmds.ls(sl=True)
			for sel in sels:
				xr, yr, zr = cmds.xform(sel, q=True, ws=True, ro=True)
				xt, yt, zt = cmds.xform(sel, q=True, ws=True, t=True)
				self.nodes[sel] = [xr, yr, zr, xt, yt, zt]

		for k, y in self.nodes.items():
			xr, yr, zr, xt, yt, zt = self.nodes[k]

			if self.nDialx.value():
				xr = self.nDialx.value()
			if self.nDialy.value():
				yr = self.nDialy.value()
			if self.nDialz.value():
				zr = self.nDialz.value()
			# if self.nSlidex.value():
			# 	xt = self.nSlidex.value()
			# if self.nSlidey.value():
			# 	yt = self.nSlidey.value()
			# if self.nSlidez.value():
			# 	zt = self.nSlidez.value()

			cmds.xform(k, ws=True, ro=[xr,yr,zr], t=[xt,yt,zt])
			self.nodes[k] = [xr, yr, zr, xt, yt, zt]

	def nTransx(self):
		for k, y in self.nodes.items():
			xr, yr, zr, xt, yt, zt = self.nodes[k]
			xt = self.nSlidex.value()
			cmds.xform(k, ws=True, t=[xt,yt,zt])
			self.nodes[k] = [xr, yr, zr, xt, yt, zt]

	def nTransy(self):
		for k, y in self.nodes.items():
			xr, yr, zr, xt, yt, zt = self.nodes[k]
			yt = self.nSlidey.value()
			cmds.xform(k, ws=True, t=[xt,yt,zt])
			self.nodes[k] = [xr, yr, zr, xt, yt, zt]

	def nTransz(self):
		for k, y in self.nodes.items():
			xr, yr, zr, xt, yt, zt = self.nodes[k]
			zt = self.nSlidez.value()
			cmds.xform(k, ws=True, t=[xt,yt,zt])
			self.nodes[k] = [xr, yr, zr, xt, yt, zt]


	def nReset(self): pass


if __name__ == '__main__':
	w = Widget()
	w.show()
