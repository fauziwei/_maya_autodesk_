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

		self.refNode = dict()
		# Import button -----------------------------------
		self.importBtn = QtWidgets.QPushButton("Import One Maya")
		self.nGridLayout = QtWidgets.QGridLayout()
		self.nGridLayout.addWidget(self.importBtn, 1, 1)
		self.setLayout(self.nGridLayout)
		self.setWindowTitle('Soovii - Bulk loader')
		self.connect(self.importBtn, QtCore.SIGNAL("clicked()"), self.nImport)

	def nImport(self):
		print '----------------------------------'
		sels = cmds.ls(sl=True)
		if not sels:
			print 'It must be empty screen, please prepare the object and select it all before import.'
			return

		self.refNode = dict()

		# Collect refNode
		for sel in sels:
			x, y, z = cmds.xform(sel, q=True, ws=True, t=True)
			self.refNode[sel] = [x,y,z]

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


		groupNode = 'BG'
		# cmds.xform(n=groupNode, ws=True,)

		i = 1
		for node in self.refNode:
			x,y,z = cmds.xform(node, q=True, ws=True, t=True)
			cmds.duplicate(groupNode)
			cmds.xform(groupNode+'%s'%i, ws=True, t=[x,y,z])
			i += 1

		cmds.delete(groupNode)



if __name__ == '__main__':
	w = Widget()
	w.show()