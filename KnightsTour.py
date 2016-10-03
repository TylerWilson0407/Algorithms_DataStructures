from pythonds.graphs import Graph, Vertex
import time

def knightGraph(bdSize):
    kg = Graph()
    for n in range(bdSize):
        for m in range(bdSize):
            nodeId = posToId(n, m, bdSize)
            genLegalMoves(kg, n, m, bdSize)
    return kg


def posToId(row, col, size):
    if (0 <= row < size) and (0 <= col < size):
        squareId = (row * size) + col
    else:
        raise IndexError('Row or column less than zero or greater than board size')
    return squareId

def genLegalMoves(g, n, m, size):
    currNode = posToId(n, m, size)
    for i in [-1, 1]:
        for j in [-2, 2]:
            if (0 <= n + i < size) and (0 <= m + j < size):
                moveNode = posToId(n + i, m + j, size)
                g.addEdge(currNode, moveNode)
            if (0 <= m + i < size) and (0 <= n + j < size):
                moveNode = posToId(m + i, n + j, size)
                g.addEdge(currNode, moveNode)

def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n + 1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

for boardSize in range(4,7):
    kg = knightGraph(boardSize)
    t1 = time.time()
    kt = knightTour(0, [], kg.getVertex(posToId(boardSize // 2, boardSize // 2, boardSize)), boardSize ** 2)
    print boardSize
    print time.time() - t1
