# Maze Generation Algorithms Using Graph Theory

## Generation Algorithms
In this section, you can access the implementations of the generation algorithms. Both the existing and modified versions are included. The modified versions are marked with a * in the title.

### Prim-Based Algorithms

### [Randomized Prim*](MazeGenerationAlgorithms/RandomizedPrim.py)  
Based on Prim’s MST method. Grows the maze by randomly selecting frontier edges from the visited region.

### [Depth First Prim*](MazeGenerationAlgorithms/DepthFirstPrim.py)  
A modified version of Prim's algorithm that prioritizes deeper exploration before branching out.

### [Initialize Prim*](MazeGenerationAlgorithms/InitalizePrim.py)  
A modified version of Prim’s algorithm that starts with a predetermined path and expands from there.

### [Loop Prim*](MazeGenerationAlgorithms/LoopPrim.py)  
A variation of Prim’s algorithm that allows loops to form in the maze.

### [Stochastic Prim*](MazeGenerationAlgorithms/StochasticPrim.py)  
A variation of Prim’s algorithm that selects the next frontier cell based on the degree of neighboring cells, introducing stochasticity.

---

### Hunt and Kill-Based Algorithms

### [Hunt and Kill](MazeGenerationAlgorithms/HuntAndKill.py)  
A random walk-based algorithm that continues until a dead end, then hunts for an unvisited cell adjacent to a visited one to resume the walk.

### [Loop Hunt and Kill*](MazeGenerationAlgorithms/LoopHuntAndKill.py)  
A variation of the Hunt and Kill algorithm designed to introduce loops into the maze.

---

### Other Algorithms

### [Aldous-Broder](MazeGenerationAlgorithms/AldousBroader.py)  
A simple random walk algorithm that starts at a random cell and moves to a random neighbor until all cells are visited.

### [DFS](MazeGenerationAlgorithms/DFS.py)  
A depth-first search algorithm that starts at a random cell and recursively visits random neighbors until all cells are visited.

### [Recursive Backtracker](MazeGenerationAlgorithms/RecursiveBacktracker.py)  
Uses recursive backtracking to explore from a random starting cell until all cells are visited.

### [Randomized Kruskal](MazeGenerationAlgorithms/RandomizedKruskal.py)  
Based on Kruskal’s MST method. Randomly removes walls between disjoint sets until all cells are connected.

### [Sidewinder](MazeGenerationAlgorithms/Sidewinder.py)  
Generates the maze row by row, carving passages eastward with occasional connections northward.

### [Wilson](MazeGenerationAlgorithms/Wilson.py)  
Generates a perfect maze using loop-erased random walks starting from randomly chosen unvisited cells.

