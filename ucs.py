import numpy as np
import random
from utils import node, problem
import heapq


def ucs(problem):
    """
    Uniform Cost Search
    :param problem: the problem
    :return: the solution node and the explored nodes
    """
    frontier = []
    heapq.heappush(frontier, node(problem.initial_state, None, None, 0))
    explored = set()
    while frontier:
        node1 = heapq.heappop(frontier)
        explored.add(node1)
        if problem.goal_test(node1.state):
            return node1, explored
        for child in problem.expand(node1):
            if child not in explored and child not in frontier:
                heapq.heappush(frontier, child)
            elif child in frontier:
                for i in frontier:
                    if i == child and i.cost > child.cost:
                        frontier.remove(i)
                        heapq.heappush(frontier, child)
    return None, explored

if __name__ == "__main__":
    # Create a problem instance
    initial_state = [4, 4, 6.3, 9, -3]
    goal_state = [-3, 4, 4, 6.3, 9]
    problem = problem(initial_state, goal_state)
    # Solve the problem
    solution,explored = ucs(problem)
    # Print the solution
    if solution is None:
        print("No solution found")
    else:
        print("Solution found")
        solution.print()
    print("number of explored nodes: ",len(explored))
