# two functions to find minimum number in list, first compare each number to every other number O(n^2).  Second O(n).
import random

def minnumfind1(lst):
    minnum = lst[0]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                minnumi = lst[i]
            else:
                minnumi = lst[j]
            if minnumi < minnum:
                minnum = minnumi
    return minnum

def minnumfind2(lst):
    minnum = lst[0]
    for i in range(len(lst)):
        if lst[i] < minnum:
            minnum = lst[i]
    return minnum

rdmlst = [int(100*random.random()) for x in range(10)]
print rdmlst
print minnumfind1(rdmlst)
print minnumfind2(rdmlst)