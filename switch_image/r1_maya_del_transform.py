import maya.cmds as cmds
 
transforms =  cmds.ls(type='transform')
deleteList = []
for tran in transforms:
    if cmds.nodeType(tran) == 'transform':
        children = cmds.listRelatives(tran, c=True) 
        if children == None:
            print '%s, has no childred' %(tran)
            deleteList.append(tran)
 
if len(deleteList) > 0:            
   cmds.delete(deleteList)