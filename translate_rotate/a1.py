# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

from PySide import QtCore
from PySide import QtGui
# import maya.cmds as cmds

class Widget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		# Spin
		# self.nSpin = QtGui.QSpinBox()
		# self.nSpin.setMinimum(1)
		# self.nSpin.setMaximum(15)

		# DIAL --------------------------------------------
		# Dial x
		self.nDialx = QtGui.QDial()
		self.nDialx.setNotchesVisible(True)
		self.nDialx.setMinimum(1)
		self.nDialx.setMaximum(20)
		self.nDialx.setValue(1) # default start from the beginning
		# Dial y
		self.nDialy = QtGui.QDial()
		self.nDialy.setNotchesVisible(True)
		self.nDialy.setMinimum(1)
		self.nDialy.setMaximum(20)
		self.nDialy.setValue(1) # default start from the beginning
		# Dial z
		self.nDialz = QtGui.QDial()
		self.nDialz.setNotchesVisible(True)
		self.nDialz.setMinimum(1)
		self.nDialz.setMaximum(20)
		self.nDialz.setValue(1) # default start from the beginning

		# SLIDE -------------------------------------------
		# Slide Horizontal X
		self.nSlidexMin, self.nSlidexMax = 1, 100 # default max 100%
		self.nSlidex = QtGui.QSlider(QtCore.Qt.Horizontal) 
		self.nSlidex.setValue( int(self.nSlidexMax/2) )

		# Slide Vertical Y
		self.nSlideyMin, self.nSlideyMax = 1, 100 # default max 100%
		self.nSlidey = QtGui.QSlider(QtCore.Qt.Vertical)
		self.nSlidey.setValue( int(self.nSlideyMax/2) ) # default vertical slide in middle

		# Slide Horizontal Z
		self.nSlidezMin, self.nSlidezMax = 1, 100 # default max 100%
		self.nSlidez = QtGui.QSlider(QtCore.Qt.Horizontal) 
		self.nSlidez.setValue( int(self.nSlidezMax/2) )

		# Close button
		self.closeBtn = QtGui.QPushButton('Close')

		self.nGridLayout = QtGui.QGridLayout()
		# self.nGridLayout.addWidget(self.nSpin, 0, 0)
		self.nGridLayout.addWidget(self.nDialx, 1, 0)
		self.nGridLayout.addWidget(self.nDialy, 1, 1)
		self.nGridLayout.addWidget(self.nDialz, 1, 2)

		self.nGridLayout.addWidget(self.nSlidex, 2, 0)
		self.nGridLayout.addWidget(self.nSlidey, 2, 1)
		self.nGridLayout.addWidget(self.nSlidez, 2, 2)

		self.nGridLayout.addWidget(self.closeBtn, 3, 1)
		self.setLayout(self.nGridLayout)
		self.setWindowTitle('Soovii - Groupees')

		# Create connection

		self.connect(self.nDialx, QtCore.SIGNAL("valueChanged(int)"), self.nRotatex)
		self.connect(self.nDialy, QtCore.SIGNAL("valueChanged(int)"), self.nRotatey)
		self.connect(self.nDialz, QtCore.SIGNAL("valueChanged(int)"), self.nRotatez)

		self.connect(self.nSlidex, QtCore.SIGNAL("valueChanged(int)"), self.nTransx)
		self.connect(self.nSlidey, QtCore.SIGNAL("valueChanged(int)"), self.nTransy)
		self.connect(self.nSlidez, QtCore.SIGNAL("valueChanged(int)"), self.nTransz)

		self.connect(self.closeBtn, QtCore.SIGNAL("clicked()"), self.close)

	def nRotatex(self): pass
	def nRotatey(self): pass
	def nRotatez(self): pass
	def nTransx(self): pass
	def nTransy(self): pass
	def nTransz(self): pass

	# def nRotate(self):
	# 	# self.nDial.setValue(1)
	# 	value = self.nDial.value()
	# 	sels = cmds.ls(sl=True)
	# 	for sel in sels:
	# 		x, y, z = cmds.xform(sel, q=True, ws=True, ro=True)
	# 		x += value
	# 		y += value
	# 		z += 
	# 		cmds.xform(sel, ws=True, ro=)


if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	w = Widget()
	w.show()
	sys.exit(app.exec_())
