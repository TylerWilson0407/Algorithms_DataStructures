import random

goal = 'methinks it is like a weasel'

charspace = 'abcdefghijklmnopqrstuvwxyz '

def randomgen(goal, charspace):
    n = len(goal)
    rdmstr = []
    for i in range(n):
        rdmstr.append(random.choice(charspace))
    return rdmstr

print randomgen(goal, charspace)

def streval(rdmstr, goal, beststr=[], bestscore=0):
    if len(rdmstr) != len(goal):
        raise RuntimeError("Input strings are not the same length")
    score = 0
    for i in range(len(rdmstr)):
        if rdmstr[i] == goal[i]:
            score += 1
    if score > bestscore:
        bestscore=score
        beststr=rdmstr
    return score, beststr, bestscore



print streval(randomgen(goal, charspace),goal)