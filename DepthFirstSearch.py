from pythonds.graphs import Graph, Vertex

class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph).__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsByFinish(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self.sortByFinish():
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    # def dfsvisitByFinish(self, startVertex):
    #     startVertex.setColor('gray')
    #     self.time += 1
    #     startVertex.setDiscovery(self.time)
    #     for nextVertex in startVertex.getConnections():
    #         if nextVertex.getColor() == 'white':
    #             nextVertex.setPred(startVertex)
    #             self.dfsvisit(nextVertex)
    #     startVertex.setColor('black')
    #     self.time += 1
    #     startVertex.setFinish(self.time)

    def sortByFinish(self):
        finList = []
        for v in self.getVertices():
            finList.append((v.getFinish(), v))
        finList.sort(key=lambda x: x[0], Reverse=True)
        return [y[1] for y in finList]

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

# Strongly connected components

def stronglyCC(g):
    g.dfs()
    gt = transposeGraph(g)
    gt.dfsByFinish()


def transposeGraph(g):
    newGraph = Graph()
    for vertex1 in g.getVertices():
        for vertex2 in vertex1.getVertices():
            if vertex1 != vertex2:
                newGraph.addEdge(vertex2, vertex1)
    return newGraph

def buildSampleGraph():
    letters = 'abcdefghi'
    sg = Graph()
    for letter in letters:
        sg.addVertex(letter)
    sg.addEdge('a', 'b')
    sg.addEdge('b', 'c')
    sg.addEdge('b', 'e')
    sg.addEdge('c', 'c')
    sg.addEdge('c', 'f')
    sg.addEdge('d', 'b')
    sg.addEdge('d', 'g')
    sg.addEdge('e', 'a')
    sg.addEdge('e', 'd')
    sg.addEdge('f', 'h')
    sg.addEdge('g', 'e')
    sg.addEdge('h', 'i')
    sg.addEdge('i', 'f')
    return sg

sg = buildSampleGraph()
