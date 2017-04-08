import maya.cmds as cmds

myHeight = 6
myCube = cmds.polyCube()
#myCube = cmds.polyCube(w=2,h=myHeight,d=2,n='block#')
#cmds.move(0,myHeight/2.0,0,myCube,r=True)
cmds.rotate(50,0,0,myCube,r=True)

sel = cmds.ls(sl=True)
#x, y, z = cmds.xform(sel, q=True, ro=True)
x, y, z = cmds.xform(sel, q=True, ws=True, ro=True)
print x, y, z
x = -1.0*x
#y = -1.0*y
#z = -1.0*z
print x, y, z
#cmds.xform(sel, r=True, ro=[x, y, z])
cmds.xform(sel, ws=True, ro=[x, y, z])
#cmds.xform(r=True, ro=[z, y, x])
#cmds.xform(p=True, roo='yzx')

