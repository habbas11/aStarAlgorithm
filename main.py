"""
 ITE - BAI501 - S21
 Dr.Bassel AlKhatib

 Participants:
 omar_108591
 omar_116205
 samar_115286
 mhd_hussam_109817
"""

from a_star import *
from node_class import Node
from romania_map_info import *

# srcNode is the node that we will start from
srcNode = Node(Arad, 0, estimationValue[Arad], Arad)

# building RomaniaGraph
RomaniaGraph = buildRomaniaMap()

# running A star algorithm from srcNode to our target `Bucharest`
# the function A_star() will return false if there is no path
if A_star(srcNode, Neamt, RomaniaGraph, RomaniaGraph.graphLen()):
    printPath(RomaniaGraph)
else:
    print('No path found')
