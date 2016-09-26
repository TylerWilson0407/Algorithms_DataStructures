# my implementation
def int2str(myint,base):
    mystr = ''
    if myint < base:
        mystr = str(myint)
    else:
        mystr = int2str((myint - (myint % base))/base,base) + str(myint % base)
    return mystr

# print int2str(332,5)

# book implementation(better)   
def toStr(n,base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]

# print toStr(332,5)

# import turtle
#
# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()
#
# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen-5)
#
# drawSpiral(myTurtle,100)
# myWin.exitonclick()

import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

# main()

import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

# def main():
#    myTurtle = turtle.Turtle()
#    myWin = turtle.Screen()
#    myPoints = [[-100,-50],[0,100],[100,-50]]
#    sierpinski(myPoints,3,myTurtle)
#    myWin.exitonclick()

# main()

# Tree - list of lists implementation

# Binary Tree

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    temp = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch, t, []])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    temp = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch, [], t])
    else:
        root.insert(2,[newBranch, [], []])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,r):
    root[0] = r

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# Binary tree - nodes & references implementation

class BinaryTree:
    def __init__(self,rootObject):
        self.key = rootObject
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self,newRoot):
        self.key = newRoot

def buildTree():
    myTree = BinaryTree('a')
    myTree.insertLeft('b')
    myTree.insertRight('c')
    myTree.getLeftChild().insertRight('d')
    myTree.getRightChild().insertLeft('e')
    myTree.getRightChild().insertRight('f')
    return myTree

# ttree = buildTree()
#
# print ttree.getRightChild().getRootVal()  # ,'c')
# print ttree.getLeftChild().getRightChild().getRootVal()  #,'d')
# print ttree.getRightChild().getLeftChild().getRootVal()  #,'e')
