#Scott Hawley

import maya.cmds as cmds
import random
import time


#create a 2d array of shapes
def shapeCreator(n, shaders):
    """
        This function creates a number of shapes, and then fills an array, it also spaces the shapes, and then scales them randomly
    """
    #create array
    shapesArray = []
    #fill array
    for x in range(n):
        tempShape = cmds.polyCube()#name = "polyCube%s"% (x)
        cmds.hyperShade(assign = shaders[x])
        cmds.setKeyframe()
        shapesArray.append(tempShape)
    #reposition each shapes
    for y in range(n):
        cmds.select(shapesArray[y])
        cmds.move(((y+1)*2),0,0)
        cmds.select(deselect = True)
    #scale each shape randomly
    for z in range(n):
        cmds.select(shapesArray[z])
        cmds.scale(1.0,random.uniform(1.0,10.0),1.0)
        cmds.select(deselect = True)
    return shapesArray
        

def bubbleSort():
    """
        This function creates and gets a list of shapes and then uses them to run a sorting algoritm
    """
    #create and get a list of shapes
    numofShapes = 10
    shaders = []
    for x in range(numofShapes):
        tempShader = cmds.shadingNode("blinn",asShader=True)
        shaders.append(tempShader)
    shapes = shapeCreator(numofShapes, shaders)
    #set some default values
    time = 0
    cmds.currentTime(time)
    #the actaul algorithm
    for passnum in range(len(shapes)-1,0,-1):
        for i in range(passnum):
            #get the y scale, and then compare which is larger
            if cmds.getAttr('pCube%s.scaleY'%(i+1)) > cmds.getAttr('pCube%s.scaleY'%(i+2)):
                #swap the two values
                #first set a keyframe of the shapes, then increase the time for the animation value, time only moves when swapping
                #cmds.select('pCube%s'%(i+1))
                #cmds.select('pCube%s'%(i+2) ,add = True)
                cmds.select(all = True)
                #change color of these two shapes during animation
                cmds.setAttr(shaders[i] + ".colorR", 1.0)
                cmds.setAttr(shaders[i] + ".colorG", 0.0)
                cmds.setAttr(shaders[i] + ".colorB", 0.0)
                
                cmds.setAttr(shaders[i+1] + ".colorR", 0.0)
                cmds.setAttr(shaders[i+1] + ".colorG", 1.0)
                cmds.setAttr(shaders[i+1] + ".colorB", 0.0)
                
                cmds.setKeyframe()
                cmds.select(deselect=True)
                time += 5
                cmds.currentTime(time)
                #temp = pCube1 ScaleY
                changeToOriginal = cmds.getAttr('pCube%s.scaleY'%(i+1))
                changeToNext = cmds.getAttr('pCube%s.scaleY'%(i+2))
                #set attribute of shapes[i].scaleY to i+1 scaleY
                cmds.setAttr('pCube%s.scaleY'%(i+1),changeToNext)
                #set attribute of shapes[i+1.scaleY to i's scaleY
                cmds.setAttr('pCube%s.scaleY'%(i+2),changeToOriginal)
                """temp = shapes[i]
                shapes[i] = shapes[i+1]
                shapes[i+1] = temp"""
                #change colors back to normal
                cmds.setAttr(shaders[i] + ".colorR", 0.5)
                cmds.setAttr(shaders[i] + ".colorG", 0.5)
                cmds.setAttr(shaders[i] + ".colorB", 0.5)
                
                cmds.setAttr(shaders[i+1] + ".colorR", 0.5)
                cmds.setAttr(shaders[i+1] + ".colorG", 0.5)
                cmds.setAttr(shaders[i+1] + ".colorB", 0.5)
    time = 0
    cmds.currentTime(time)
        
cmds.file(new = True, f = True)
cmds.autoKeyframe(state = True)
random.seed(time.time())
bubbleSort()