from dataclasses import dataclass


# We need a data structure that can hold 4 values
# - A node name
# - A node actual cost
# - A node estimationCost
# - A node total cost

@dataclass
class Node:
    name: int
    actualCost: int
    estimationCost: int
    totCost: int

    # total cost = actual cost + estimation cost
    def __post_init__(self):
        self.totCost = self.actualCost + self.estimationCost

    # in order to be able to iterate over Node variables
    def __iter__(self):
        return [self.actualCost, self.estimationCost, self.totCost]
