# Maze Generation Algorithms Using Graph Theory

## Generation Algorithms
In this section, you can access the implementations of the generation algorithms. Both the existing and modified versions are included. The modified versions are marked with a * in the title.

### Aldous-Broder
This algorithm is a simple random walk algorithm that starts at a random cell and moves to a random neighbor until all cells are visited.

### Depth First Prim*
This algorithm is a modified version of Prim's algorithm that prioritizes deeper exploration into the maze before branching out.

### DFS
This algorithm is a simple depth-first search algorithm that starts at a random cell and moves to a random neighbor until all cells are visited.

### [Hunt and Kill](MazeGenerationAlgorithms/HuntAndKill.py)  
This algorithm is a variation of the random walk approach. It randomly walks through unvisited neighbors until it reaches a dead end, then hunts for the next unvisited cell adjacent to a visited one to continue the process.

