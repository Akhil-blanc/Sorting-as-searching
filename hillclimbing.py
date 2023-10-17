import numpy as np
import random
from utils import node, problem

def heuristic(state, goal):
    """
    Heuristic function
    :param state: the state
    :param goal: the goal state
    :return: the heuristic value
    """
    return np.linalg.norm(np.array(state) - np.array(goal))

class node(node):
    """
    Node class for astar search
    """
    def __init__(self, state, parent, action, path_cost, heuristic):
        """
        Constructor
        :param state: the state
        :param parent: the parent node
        :param action: the action
        :param path_cost: the path cost
        :param heuristic: the heuristic value
        """
        super().__init__(state, parent, action, path_cost)
        self.heuristic = heuristic

    def __lt__(self, other):
        """
        Less than operator
        :param other: the other node
        :return: True if the node is less than the other node, False otherwise
        """
        return self.heuristic< other.heuristic
    
    def __eq__(self, other):
        """
        Equal operator
        :param other: the other node
        :return: True if the node is equal to the other node, False otherwise
        """
        return self.state == other.state
    
    def __hash__(self):
        return super().__hash__()
    
class problem(problem):
    """
    Problem class for greedy search
    """
    def __init__(self, initial_state, goal_state):
        """
        Constructor
        :param initial_state: the initial state
        :param goal_state: the goal state
        """
        super().__init__(initial_state, goal_state)

    def expand(self, node1):
        """
        :param node: the node to expand
        :return: a list of nodes that are the children of the given node
        """
        children = []
        for i in range(len(node1.state)):
            for j in range(i + 1, len(node1.state)):
                child = list(node1.state)
                child[i], child[j] = child[j], child[i]
                children.append(node(child, node1,(child[i],child[j]), node1.cost + 1, heuristic(child, self.goal_state)))
        return children

def hillclimbing(problem):
    """
    Hill climbing search
    :param problem: the problem
    :return: the solution node
    """
    current = node(problem.initial_state, None, None, 0, heuristic(problem.initial_state, problem.goal_state))
    while True:
        neighbors = problem.expand(current)
        if not neighbors:
            break
        neighbor = min(neighbors)
        if neighbor.heuristic >= current.heuristic:
            break
        current = neighbor
    return current

if __name__ == "__main__":
    # Create a problem instance
    initial_state = [4, 4, 6.3, 9, -3]
    goal_state = [-3, 4, 4, 6.3, 9]
    problem = problem(initial_state, goal_state)
    # Solve the problem
    solution = hillclimbing(problem)
    # Print the solution
    solution.print()
    print("number of explored nodes: ",len(list(solution.path())))