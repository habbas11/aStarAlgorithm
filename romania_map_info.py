from graph_class import Graph

# Assigning each city to a number for easy access
Arad = 0
Bucharest = 1
Craiova = 2
Dodreta = 3
Eforie = 4
Fagaras = 5
Giurgiu = 6
Hirsova = 7
Lasi = 8
Lugoj = 9
Mehadia = 10
Neamt = 11
Oradea = 12
Pitesti = 13
Rimnicu_Vilcea = 14
Sibiu = 15
Timisoara = 16
Urziceni = 17
Vaslui = 18
Zerind = 19

# A dictionary for getting the name of each city
citiesId = {
    0: 'Arad',
    1: 'Bucharest',
    2: 'Craiova',
    3: 'Dodreta',
    4: 'Eforie',
    5: 'Fagaras',
    6: 'Giurgiu',
    7: 'Hirsova',
    8: 'Lasi',
    9: 'Lugoj',
    10: 'Mehadia',
    11: 'Neamt',
    12: 'Oradea',
    13: 'Pitesti',
    14: 'Rimnicu_Vilcea',
    15: 'Sibiu',
    16: 'Timisoara',
    17: 'Urziceni',
    18: 'Vaslui',
    19: 'Zerind',
}

# the default estimation values
estimationValue = [366, 0, 160, 242, 161,
                   178, 77, 151, 226, 244,
                   241, 234, 380, 98, 193,
                   253, 329, 80, 199, 374]


# build Romania map by building edges among cities with their costs
def buildRomaniaMap():
    RomaniaGraph = Graph()

    RomaniaGraph.addEdge(Arad, Zerind, 75)
    RomaniaGraph.addEdge(Arad, Sibiu, 140)
    RomaniaGraph.addEdge(Arad, Timisoara, 118)

    RomaniaGraph.addEdge(Zerind, Oradea, 71)

    RomaniaGraph.addEdge(Oradea, Sibiu, 151)

    RomaniaGraph.addEdge(Timisoara, Lugoj, 111)

    RomaniaGraph.addEdge(Lugoj, Mehadia, 70)

    RomaniaGraph.addEdge(Mehadia, Dodreta, 75)

    RomaniaGraph.addEdge(Dodreta, Craiova, 120)

    RomaniaGraph.addEdge(Craiova, Rimnicu_Vilcea, 146)
    RomaniaGraph.addEdge(Craiova, Pitesti, 138)

    RomaniaGraph.addEdge(Sibiu, Rimnicu_Vilcea, 80)
    RomaniaGraph.addEdge(Sibiu, Fagaras, 99)

    RomaniaGraph.addEdge(Fagaras, Bucharest, 211)

    RomaniaGraph.addEdge(Rimnicu_Vilcea, Pitesti, 97)

    RomaniaGraph.addEdge(Pitesti, Bucharest, 101)

    RomaniaGraph.addEdge(Bucharest, Giurgiu, 90)
    RomaniaGraph.addEdge(Bucharest, Urziceni, 85)

    RomaniaGraph.addEdge(Urziceni, Hirsova, 98)
    RomaniaGraph.addEdge(Urziceni, Vaslui, 142)

    RomaniaGraph.addEdge(Hirsova, Eforie, 86)

    RomaniaGraph.addEdge(Vaslui, Lasi, 92)

    RomaniaGraph.addEdge(Lasi, Neamt, 87)
    # finally return the made up graph
    return RomaniaGraph


# openList for nodes that we are exploring
openList = []
# visited is a bool list for checking if a node is added to openList
visited = [False for a in range(0, 20)]
# closeList is a bool list for nodes that we are done with
closeList = [0 for b in range(0, 20)]
# parent list for assigning the parent of each node
parent = [-1 for c in range(0, 20)]
