# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

import os
from PySide import QtCore
from PySide import QtGui

import maya.cmds as cmds

reload(sys)
sys.setdefaultencoding('utf-8')

class Widget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		self.refNode = dict() # Existing reference nodes in screen
		self.copyNode = dict() # the node which is duplicate itself

		# Import button -----------------------------------
		self.importBtn = QtGui.QPushButton("Import Bulk Maya's files")

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

		# Reset button ----------------------------------
		self.resetBtn = QtGui.QPushButton('Reset')
		# Clear all nodes ------------------------------
		# self.clearBtn = QtGui.QPushButton('Clear')
		# Close button ----------------------------------
		self.closeBtn = QtGui.QPushButton('Close')


		# Layout
		self.nGridLayout = QtGui.QGridLayout()
		# import
		self.nGridLayout.addWidget(self.importBtn, 1, 1)
		# dial
		self.nGridLayout.addWidget(self.nDialx, 2, 0)
		self.nGridLayout.addWidget(self.nDialy, 2, 1)
		self.nGridLayout.addWidget(self.nDialz, 2, 2)
		# slide
		self.nGridLayout.addWidget(self.nSlidex, 3, 0)
		self.nGridLayout.addWidget(self.nSlidey, 3, 1)
		self.nGridLayout.addWidget(self.nSlidez, 3, 2)
		# reset, clear and close
		self.nGridLayout.addWidget(self.resetBtn, 4, 0)
		# self.nGridLayout.addWidget(self.clearBtn, 4, 1)
		self.nGridLayout.addWidget(self.closeBtn, 4, 2)

		self.setLayout(self.nGridLayout)
		self.setWindowTitle('Soovii - Bulk loader')

		# Create connection
		# import
		self.connect(self.importBtn, QtCore.SIGNAL("clicked()"), self.nImport)
		# dial
		self.connect(self.nDialx, QtCore.SIGNAL("valueChanged(int)"), self.nRT)
		self.connect(self.nDialy, QtCore.SIGNAL("valueChanged(int)"), self.nRT)
		self.connect(self.nDialz, QtCore.SIGNAL("valueChanged(int)"), self.nRT)
		# slide
		self.connect(self.nSlidex, QtCore.SIGNAL("valueChanged(int)"), self.nRT)
		self.connect(self.nSlidey, QtCore.SIGNAL("valueChanged(int)"), self.nRT)
		self.connect(self.nSlidez, QtCore.SIGNAL("valueChanged(int)"), self.nRT)
		# reset, clear and close
		self.connect(self.resetBtn, QtCore.SIGNAL("clicked()"), self.nReset)
		self.connect(self.closeBtn, QtCore.SIGNAL("clicked()"), self.close)

	# Load bulk files in a folder
	def nImport(self):
		# Initialize reference nodes
		sels = cmds.ls(sl=True)
		if not sels:
			print 'It must be empty screen, please prepare the object and select it all before import.'
			return
		for sel in sels:
			x, y, z = cmds.xform(sel, q=True, ws=True, rt=True)
			self.refNode[sel] = [x, y, z]

		# Load one new node, this automatically should be copied adjusting number of existing node
		currentDir = ''
		filters = 'Maya (*.ma *mb)'
		homeDir = os.getenv('HOME')
		dirCache = os.path.join(homeDir, 'dir_cache_bulk_loader.txt')
		if os.path.exists(dirCache):
			with open(dirCache) as f:
				currentDir = f.read()
		else:
			currentDir = QtCore.QDir.currentPath()

		files, _ = QtGui.QFileDialog.getOpenFileNames(self, "Folder", dir=currentDir, filter=filters)

		if not len(files) == 0:
			currentDir = os.path.dirname(files[0])
			with open(dirCache, 'w') as f:
				f.write('%s' % currentDir)


		# The loading file must contain only single node
		for f in files:
			print '%s' % f
			cmds.file(f, i=True)

		# Get the new node
		singleNode = None
		sels = cmds.ls(sl=True)
		for sel in sels:
			if sel not in self.refNode:
				singleNode = sel
				break

		for k, v in self.refNode.items():
			node = cmds.duplicate(singleNode)
			cmds.xform(node, ws=True, rt=v)
			self.copyNode[node] = v

		cmds.delete(singleNode)
		cmds.select(all=True)

	# Rotation (ro) and RotationTranslation (rt)
	def nRT(self):
		sels = cmds.ls(sl=True)
		if len(self.default) == 0:
			for sel in sels:
				xo, yo, zo = cmds.xform(sel, q=True, ws=True, ro=True)
				xt, yt, zt = cmds.xform(sel, q=True, ws=True, rt=True)
				self.default[sel] = [xo, yo, zo, xt, yt, zt]

		for sel in sels:
			xo, yo, zo = cmds.xform(sel, q=True, ws=True, ro=True)
			xt, yt, zt = cmds.xform(sel, q=True, ws=True, rt=True)
			xo = self.nDialx.value() if self.nDialx.value() else xo
			yo = self.nDialy.value() if self.nDialy.value() else yo
			zo = self.nDialz.value() if self.nDialz.value() else zo
			xt = self.nSlidex.value() if self.nSlidex.value() else xt
			yt = self.nSlidey.value() if self.nSlidey.value() else yt
			zt = self.nSlidez.value() if self.nSlidez.value() else zt
			cmds.xform(sel, ws=True, ro=[xo, yo, zo], rt=[xt, yt, zt])

	def nReset(self):
		if len(self.copyNode)>0:
			cmds.delete(self.copyNode)



if __name__ == '__main__':
	w = Widget()
	w.show()
