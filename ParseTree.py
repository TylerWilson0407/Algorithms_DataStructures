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

pt = buildParseTree(' ( 3 + ( 7 + 4 ) ) ')
pt.postorder()
print '###'
pt.preorder()
print '###'
pt.inorder()
print '###'

import operator

def evaluate(pt):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    if pt.getLeftChild() == None:
        return pt.getRootVal()
    else:
        op = operators[pt.getRootVal()]
        return op(evaluate(pt.getLeftChild()), evaluate(pt.getRightChild()))

print evaluate(pt)