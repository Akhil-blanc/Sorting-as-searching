# Folder
The folder contains the following files:
* [Readme.md](Readme.md) - this file
* [bfs.py](bfs.py) - the implementation of the BFS algorithm
* [dfs.py](dfs.py) - the implementation of the DFS algorithm
* [ucs.py](ucs.py) - the implementation of the UCS algorithm
* [astar.py](astar.py) - the implementation of the A* algorithm
* [iterative_deepening.py](iterative_deepening.py) - the implementation of the iterative deepening algorithm
* [greedy_search.py](greedy_search.py) - the implementation of the greedy search algorithm
* [utils.py](utils.py) - the implementation of problem class and node class
* [hill_climbing.py](hill_climbing.py) - the implementation of the hill climbing algorithm
* [partb.ipynb](partb.ipynb) - the solution notebook for part b

# Problem
The problem is to find the path from the start node to the goal node. The problem is implemented in the problem class in utils.py. The problem class contains the following attributes:
* start: the start node
* goal: the goal node
follwing methods:
* goal_test: check if the node is the goal node
* expand: expand the node to get its children

# Node
The node class is implemented in utils.py. The node class contains the following attributes:
* state: the state of the node
* parent: the parent node
* action: the action to get to the node
* cost: the path cost to get to the node
follwoing methods:
* print: prints node state, cost and path taken to reach the node
* path: returns the path taken to reach the node

# BFS
The BFS algorithm is implemented in bfs.py. The BFS algorithm uses a FIFO queue to store the nodes. The BFS algorithm is implemented in the bfs function. The bfs function takes a problem as input and returns the goal node. The bfs function uses the following variables:
* problem: object of problem class

# DFS
The DFS algorithm is implemented in dfs.py. The DFS algorithm uses a LIFO queue to store the nodes. The DFS algorithm is implemented in the dfs function. The dfs function takes a problem as input and returns the goal node. The dfs function uses the following variables:
* problem: object of problem class

# UCS
The UCS algorithm is implemented in ucs.py. The UCS algorithm uses a priority queue to store the nodes. The UCS algorithm is implemented in the ucs function. The ucs function takes a problem as input and returns the goal node. The ucs function uses the following variables:
* problem: object of problem class

# A*

The A* algorithm is implemented in astar.py. The A* algorithm uses a priority queue to store the nodes. The A* algorithm is implemented in the astar function. The astar function takes a problem as input and returns the goal node. The astar function uses the following variables:
* problem: object of problem class

heuristic function:
equal to 0 as we are immitating is a uniform cost search problem

# Iterative Deepening
The iterative deepening algorithm is implemented in iterative_deepening.py. The iterative deepening algorithm is implemented in the iterative_deepening function. The iterative_deepening function takes a problem as input and returns the goal node. The iterative_deepening function uses the following variables:
* problem: object of problem class

functions used:
* depth_limited_search: performs depth limited search
* iterative_deepening: performs iterative deepening search

# Greedy Search
The greedy search algorithm is implemented in greedy_search.py. The greedy search algorithm uses a priority queue to store the nodes. The greedy search algorithm is implemented in the greedy_search function. The greedy_search function takes a problem as input and returns the goal node. The greedy_search function uses the following variables:
* problem: object of problem class

heuristic function:
equal to number of misplaced numbers

# Hill Climbing
The hill climbing algorithm is implemented in hill_climbing.py. The hill climbing algorithm is implemented in the hill_climbing function. The hill_climbing function takes a problem as input and returns the goal node. The hill_climbing function uses the following variables:
* problem: object of problem class

heuristic function:
equal to norm of difference between current state and goal state

# Part B
functions used:
* generate_random_start_state: generates a random start state
* get_avg_nodes: returns the average number of nodes explored


