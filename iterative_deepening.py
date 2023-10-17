import numpy as np
import random
from utils import node,problem

def depth_limited_search(problem, limit):
    """
    Depth-limited search algorithm
    :param problem: the problem to solve
    :param limit: the depth limit
    :return: the solution node
    """
    # Initialize the frontier using the initial state of problem
    frontier = []
    frontier.append(node(problem.initial_state, None, None, 0))
    # Initialize the explored set to be empty
    explored = set()
    # Repeat
    while True:
        # If the frontier is empty then return failure
        if len(frontier) == 0:
            return None
        # Choose a leaf node and remove it from the frontier
        leaf = frontier.pop()
        # If the node contains a goal state then return the corresponding solution
        if problem.goal_test(leaf.state):
            return leaf,explored
        # Add the node to the explored set
        explored.add(leaf)
        # Expand the chosen node, adding the resulting nodes to the frontier
        if leaf.cost < limit:
            for child in problem.expand(leaf):
                if child not in explored and child not in frontier:
                    frontier.append(child)

def iterative_deepening(problem):
    """
    Iterative deepening search algorithm
    :param problem: the problem to solve
    :return: the solution node
    """
    # Repeat
    count=1
    while True:
        # Run a depth-limited search with depth limit = depth
        result = depth_limited_search(problem, count)
        # If the search finds a solution then return it
        if result is not None:
            return result
        count+=1

if __name__ == "__main__":
    # Create a problem instance
    initial_state = [4, 4, 6.3, 9, -3]
    goal_state = [-3, 4, 4, 6.3, 9]
    problem= problem(initial_state, goal_state)
    # Solve the problem
    solution,explored = iterative_deepening(problem)
    # Print the solution
    if solution is None:
        print("No solution found")
    else:
        print("Solution found")
        solution.print()
    print("number of explored nodes: ",len(explored))