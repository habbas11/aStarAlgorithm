class Graph:
    # initializing graph as a 2D array, where the value is the cost of the edge
    # between two nodes
    def __init__(self):
        graph = [[-1 for x in range(0, 20)] for y in range(0, 20)]
        self._graph = graph

    # building the graph, by making edges with cost
    def addEdge(self, fromNode, toNode, cost):
        self._graph[fromNode][toNode] = cost
        self._graph[toNode][fromNode] = cost

    # return the value of the cost of an edge between two nodes
    def getEdge(self, fromNode, toNode):
        return self._graph[fromNode][toNode]

    # return the length of the 2D array (the graph)
    def graphLen(self):
        return len(self._graph)

    # for testing purposes
    def print_graph(self):
        for i in range(0, self.graphLen()):
            print(self._graph[i])
