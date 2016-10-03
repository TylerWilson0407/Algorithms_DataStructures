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
