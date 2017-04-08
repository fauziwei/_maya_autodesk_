# coding: utf-8
'''Fauzi, fauzi@soovii.com'''

import os
import sys
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

import maya.cmds as cmds

reload(sys)
sys.setdefaultencoding('utf-8')

class Widget(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)

		self.allNodes = [] # just grab all in screen
		self.refNode = dict() # Existing reference nodes in screen
		self.copyNode = dict() # the node which is duplicate itself

		# Import button -----------------------------------
		self.importBtn = QtWidgets.QPushButton("Import One Maya")

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

		# Reset button ----------------------------------
		self.resetBtn = QtWidgets.QPushButton('Reset')
		# Close button ----------------------------------
		self.closeBtn = QtWidgets.QPushButton('Close')


		# Layout
		self.nGridLayout = QtWidgets.QGridLayout()
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
		print '----------------------------------'
		# Initialize reference nodes
		sels = cmds.ls(sl=True)
		if not sels:
			print 'It must be empty screen, please prepare the object and select it all before import.'
			return

		self.nReset()

		self.allNodes = [] # just grab all in screen
		self.refNode = dict() # Existing reference nodes in screen
		self.copyNode = dict() # the node which is duplicate itself

		# Collect refNode
		for sel in sels:
			# x, y, z = cmds.xform(sel, q=True, ws=True, t=True)
			x, y, z = cmds.xform(sel, q=True, wd=True, t=True)
			self.refNode[sel] = [x,y,z]
			print '%s: %s' % (sel,[x,y,z])

		# Collect all nodes in screen unless refNode
		sels = cmds.ls(type='transform')
		for sel in sels:
			if sel not in self.refNode:
				self.allNodes.append(sel)

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

		files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Folder", dir=currentDir, filter=filters)

		if not len(files) == 0:
			currentDir = os.path.dirname(files[0])
			with open(dirCache, 'w') as f:
				f.write('%s' % currentDir)

		# The loading file must contain only single node
		for f in files:
			print 'load file: %s' % f
			cmds.file(f, i=True)

		origCopyNode = None
		sels = cmds.ls(type='transform')
		for sel in sels:
			if sel not in self.refNode:
				if sel not in self.allNodes:
					origCopyNode = sel

		# Duplicate copyNode adjust to refNode
		for k, v in self.refNode.items():
			cmds.duplicate(origCopyNode)

		sels = cmds.ls(type='transform')
		for sel in sels:
			if sel not in self.refNode:
				if sel not in self.allNodes:
					self.copyNode[sel] = ['a',0,0]

		del self.copyNode[origCopyNode]
		cmds.delete(origCopyNode)

		# move position copyNode regard to refNode
		for k, v in self.refNode.items():
			for i, j in self.copyNode.items():
				if j[0]=='a':
					print '%s: %s' % (i, v)
					# cmds.xform(i, ws=True, t=v)
					cmds.xform(i, wd=True, t=v)
					self.copyNode[i] = v
					break


	# Rotation (ro) and RotationTranslation (rt)
	def nRT(self):
		sels = self.refNode
		if len(self.copyNode)>0:
			sels.update(self.copyNode)

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
			cmds.delete(self.copyNode.keys())
			self.copyNode = dict()



if __name__ == '__main__':
	w = Widget()
	w.show()
