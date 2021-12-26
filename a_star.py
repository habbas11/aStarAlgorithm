import operator
from node_class import Node
from romania_map_info import *


def A_star(src, target, graph, graphLen):
    openList.append(src)
    # sort openList according to totCost	
    openList.sort(key=operator.attrgetter('totCost'))

    while len(openList) > 0:
        # currentNode is the node with the least actual cost, since we have sorted openList
        currentNode = openList[0]
        # check if the current node is the target, if so then return True to indicate that there is a valid path
        if currentNode.name == target:
            return True
        # remove currentNode from openList
        openList.pop(0)
        # mark the current node as not visited (not in the openList)
        visited[currentNode.name] = False
        # add the current node to the closeList
        closeList[currentNode.name] = True

        # Traversing the children nodes of the current node node
        for i in range(0, graphLen):
            # check if there is an edge between currentNode and i, and that i is not in closeList
            if graph.getEdge(currentNode.name, i) != -1 and not closeList[i]:
                # if i is in the openList
                if visited[i]:
                    # loop throw the openList to find node i index in it
                    j = 0
                    for k in range(0, len(openList)):
                        j += 1
                        if openList[k].name == i:
                            break

                    # update node i
                    cost = currentNode.actualCost + graph.getEdge(currentNode.name, i)
                    if cost < openList[j].actualCost:
                        # update i actual cost
                        openList[j].actualCost = cost
                        # update i total cost
                        openList[j].totCost = cost + openList[j].estimationCost
                        # update i parent
                        parent[i] = currentNode.name
                # if i has not been added to openList yet, a new node will be created and added to the openList
                else:
                    newNode = Node(i, graph.getEdge(currentNode.name, i), estimationValue[i], currentNode.name)
                    parent[i] = currentNode.name
                    openList.append(newNode)
                    openList.sort(key=operator.attrgetter('totCost'))
                    visited[i] = True
    # return False if there is no valid path
    return False


def printPath(graph):
    # lastNode is the node that is supposed to be the target node
    lastNode = openList[0].name
    # add lastNode to the path
    path = [lastNode]
    # and then add its parent, and the parent of its parent...
    while parent[lastNode] != -1:
        path.append(parent[lastNode])
        lastNode = parent[lastNode]

    # reverse the path list
    path = path[::-1]

    # cost is the total cost needed if following the found path
    cost = 0

    print('Shortest Path: ', end='')

    # print the path
    for i in range(0, len(path)):
        if i + 1 < len(path):
            print(citiesId[path[i]], '-> ', end='')
        else:
            print(citiesId[path[i]])

        if i + 1 < len(path):
            # add the cost of all the edges
            cost += graph.getEdge(path[i], path[i + 1])

    print('Total cost =', cost)
