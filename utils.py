import numpy as np

class node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def print(self):
        print("state: ",self.state)
        print("path cost: ",self.cost)
        print("path: ")
        for i in self.path():
            print("action: swap",i.action)
            print(i.state)

    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    def __hash__(self):
        return hash(str(self.state))
    
class problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, state):
        return state == self.goal_state

    def expand(self, node1):
        children = []
        for i in range(len(node1.state)):
            for j in range(i + 1, len(node1.state)):
                child = list(node1.state)
                child[i], child[j] = child[j], child[i]
                children.append(node(child, node1, (child[i], child[j]), node1.cost + 1))
        return children