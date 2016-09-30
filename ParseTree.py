from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

"""
build parse tree from fully parenthesized expression, evaluate the parse tree, and recover the expression from the tree
"""

def buildParseTree(expr):
    exlist = expr.split()
    tStack = Stack()
    operators = ['*', '/', '+', '-']
    pt = BinaryTree('')
    tStack.push(pt)

    for i in exlist:
        if i == '(':
            pt.insertLeft('')
            tStack.push(pt)
            pt = pt.getLeftChild()
        elif i not in (operators + [')']):
            pt.setRootVal(int(i))
            pt = tStack.pop()
        elif i in operators:
            pt.setRootVal(i)
            pt.insertRight('')
            tStack.push(pt)
            pt = pt.getRightChild()
        elif i == ')':
            pt = tStack.pop()
        else:
            raise ValueError
    return pt

pt = buildParseTree(' ( ( 8 + 5 ) * ( 3 + ( 7 - 4 ) ) ) ')
# pt.postorder()
# print '###'
# pt.preorder()
# print '###'
# pt.inorder()
# print '###'

import operator

def evaluate(pt):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if pt.getLeftChild() == None:
        return pt.getRootVal()
    else:
        op = operators[pt.getRootVal()]
        return op(evaluate(pt.getLeftChild()), evaluate(pt.getRightChild()))

# print evaluate(pt)

def preorder(pt):
    if pt:
        print pt.getRootVal()
        preorder(pt.getLeftChild())
        preorder(pt.getRightChild())

# preorder(pt)
# print '###'

def inorder(pt):
    if pt:
        inorder(pt.getLeftChild())
        print pt.getRootVal()
        inorder(pt.getRightChild())

def postorder(pt):
    if pt:
        postorder(pt.getLeftChild())
        postorder(pt.getRightChild())
        print pt.getRootVal()

# inorder(pt)
# print '###'
# postorder(pt)
# print '###'

def postordereval(pt):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if pt:
        if pt.getRightChild() and pt.getLeftChild():
            return operators[pt.getRootVal()](postordereval(pt.getLeftChild()), postordereval(pt.getRightChild()))
        else:
            return pt.getRootVal()

# print postordereval(pt)

def printexpr(pt):
    sVal = ''
    if pt and not (pt.getLeftChild() and pt.getRightChild()):
        sVal = printexpr(pt.getLeftChild())
        sVal = sVal + str(pt.getRootVal())
        sVal = sVal + printexpr(pt.getRightChild())
    elif pt:
        sVal = '(' + printexpr(pt.getLeftChild())
        sVal = sVal + str(pt.getRootVal())
        sVal = sVal + printexpr(pt.getRightChild()) + ')'
    return sVal

# print printexpr(pt)

from pythonds.trees.binheap import BinHeap

# bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)
#
# print(bh.delMin())
#
# print(bh.delMin())
#
# print(bh.delMin())
#
# print(bh.delMin

