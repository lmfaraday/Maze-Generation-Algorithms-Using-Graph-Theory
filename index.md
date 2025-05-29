# Maze Generation Algorithms Using Graph Theory

## Generation Algorithms
In this section, you can access the implementations of the generation algorithms. Both the existing and modified versions are included. The modified versions are marked with a * in the title.

### Prim-Based Algorithms

### [Randomized Prim](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RandomizedPrim.py)  
Based on Prim’s MST method. Grows the maze by randomly selecting frontier edges from the visited region.

### [Depth First Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/DepthFirstPrim.py)  
A modified version of Prim's algorithm that prioritizes deeper exploration before branching out.

### [Initialized Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/InitializedPrim.py)  
A modified version of Prim’s algorithm that starts with a predetermined path and expands from there.

### [Loop Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/LoopPrim.py)  
A variation of Prim’s algorithm that allows loops to form in the maze.

### [Stochastic Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/StochasticPrim.py)  
A variation of Prim’s algorithm that selects the next frontier cell based on the degree of neighboring cells, introducing stochasticity.

---

### Hunt and Kill-Based Algorithms

### [Hunt and Kill](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/HuntAndKill.py)  
A random walk-based algorithm that continues until a dead end, then hunts for an unvisited cell adjacent to a visited one to resume the walk.

### [Loop Hunt and Kill*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/LoopHuntAndKill.py)  
A variation of the Hunt and Kill algorithm designed to introduce loops into the maze.

---

### Other Algorithms

### [Aldous-Broder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/AldousBroder.py)  
A simple random walk algorithm that starts at a random cell and moves to a random neighbor until all cells are visited.

### [DFS](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/DFS.py)  
A depth-first search algorithm that starts at a random cell and recursively visits random neighbors until all cells are visited.

### [Recursive Backtracker](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RecursiveBacktracker.py)  
Uses recursive backtracking to explore from a random starting cell until all cells are visited.

### [Randomized Kruskal](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RandomizedKruskal.py)  
Based on Kruskal’s MST method. Randomly removes walls between disjoint sets until all cells are connected.

### [Sidewinder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/Sidewinder.py)  
Generates the maze row by row, carving passages eastward with occasional connections northward.

### [Wilson](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/Wilson.py)  
Generates a perfect maze using loop-erased random walks starting from randomly chosen unvisited cells.

## Solution Algorithms
In this section, you can access the implementations of the generation algorithms. Both the existing and modified versions are included. The modified versions are marked with a * in the title.

### [A*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/AStar.py)  
Uses a heuristic to efficiently find the shortest path from the start to the goal, combining features of uniform-cost search and greedy search.

### [Breadth First Search](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/BreadthFirstSearch.py)
Explores all nodes at the current depth level before moving to the next, guaranteeing the shortest path in an unweighted maze.

### [Depth First Search](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/DepthFirstSearch.py)
Explores as far as possible along each branch before backtracking. Not guaranteed to find the shortest path.

### [Hybrid Search*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/HybridSearch.py)
A custom combination of multiple search strategies designed to balance exploration and optimality.

### [Random Walk](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/RandomWalk.py)
Chooses the next move randomly without memory or goal orientation. 

### [Hand on Wall](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/HandOnWall.py)
Follows the left or right wall consistently. Works only in simply-connected mazes (no loops inside).

### [Deep Q-Learning*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/DeepQNetwork.ipynb)
A reinforcement learning approach that uses a neural network to approximate the Q-value function, allowing the agent to learn optimal policies for maze navigation.
