import numpy as np
import queue
import random
from utils import node,problem


def bfs(problem):
    """
    Breadth-first search algorithm
    :sort the numbers: the problem to solve
    :return: the solution node
    """
    # Initialize the frontier using the initial state of problem
    frontier = queue.Queue()
    frontier.put(node(problem.initial_state, None, None, 0))
    # Initialize the explored set to be empty
    explored = set()
    # Repeat
    while True:
        # If the frontier is empty then return failure
        if frontier.empty():
            return None
        # Choose a leaf node and remove it from the frontier
        leaf = frontier.get()
        # If the node contains a goal state then return the corresponding solution
        
        if problem.goal_test(leaf.state):
            return (leaf,explored)
        # Add the node to the explored set
        explored.add(leaf)
        # Expand the chosen node, adding the resulting nodes to the frontier
        for child in problem.expand(leaf):
            if child not in explored and child not in frontier.queue:
                frontier.put(child)

if __name__ == "__main__":
    # Create a problem instance
    initial_state = [4, 4, 6.3, 9, -3]
    goal_state = [-3, 4, 4, 6.3, 9]
    problem = problem(initial_state, goal_state)
    # Solve the problem
    solution,explored = bfs(problem)
    # Print the solution
    if solution is None:
        print("No solution found")
    else:
        print("Solution found")
        solution.print()
    print("number of explored nodes: ",len(explored))
