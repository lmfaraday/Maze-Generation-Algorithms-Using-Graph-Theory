📄 **Full Project Report:**  
Access the complete project report **[here](#)**.  

---

💻 **Explore the Code:**  
Source code are available on the  
[GitHub Repository](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory).  
Feel free to dive in and explore!

---

📌 This is a comprehensive project developed as part of the **Industrial Engineering Graduation Project** at **Boğaziçi University**.

The project focuses on generating mazes of varying structural complexity using **graph-based algorithms**, and solving them through **classical** and **reinforcement learning** techniques in specific **Deep Q-Network (DQN)**. After generation and solution processes, the mazes are **sampled and analyzed** to understand how structural features affect solvability and agent behavior.

---

## 📂 Table of Contents

- [Maze Generation Algorithms](#maze-generation-algorithms)  
  - [Prim-Based](#prim-based)  
  - [Hunt and Kill-Based](#hunt-and-kill-based)  
  - [Other Algorithms](#other-algorithms)  
- [Maze Solution Algorithms](#maze-solution-algorithms)  
- [Maze Visualizations and Animations](#-maze-visualizations-and-animations)
- [Data & Evaluation](#-data--evaluation)

---

## 🧩 Maze Generation Algorithms

Maze generation is the core of this project. All mazes are generated on **grid graphs**, where nodes represent cells and edges represent possible passages. The algorithms vary in their logic, ranging from randomized traversal to minimum spanning tree-based structures.

> **Note:** Algorithms marked with a * have been modified or developed by us.

Generation algorithms included in this project, in specific:
### Prim-Based
A collection of Prim's algorithm variations for maze generation, including our custom modifications that introduce different traversal patterns and initialization strategies.

- 🔗 [Randomized Prim](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RandomizedPrim.py) - Classic implementation using random edge selection
- 🔗 [Depth First Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/DepthFirstPrim.py) - Modified to prioritize depth-first traversal patterns
- 🔗 [Initialized Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/InitializedPrim.py) - Custom initialization strategy for controlled maze structure
- 🔗 [Loop Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/LoopPrim.py) - Introduces controlled loops in the maze structure
- 🔗 [Stochastic Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/StochasticPrim.py) - Adds probabilistic edge selection for varied patterns

### Hunt and Kill-Based
Hunt and Kill algorithm implementations that create mazes through a combination of random walks and systematic hunting for unvisited cells.

- 🔗 [Hunt and Kill](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/HuntAndKill.py) - Standard implementation alternating between random walks and hunting
- 🔗 [Loop Hunt and Kill*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/LoopHuntAndKill.py) - Modified version that introduces controlled loops

### Other Algorithms
A diverse set of maze generation algorithms, each with unique characteristics in terms of randomness, bias, and generation patterns.

- 🔗 [Aldous-Broder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/AldousBroder.py) - Uniform spanning tree algorithm using random walks
- 🔗 [Randomized Depth First Search (DFS)](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/DFS.py) - Classic DFS with randomized neighbor selection
- 🔗 [Recursive Backtracker](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RecursiveBacktracker.py) - Stack-based implementation of DFS maze generation
- 🔗 [Randomized Kruskal](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RandomizedKruskal.py) - Minimum spanning tree algorithm with random edge selection
- 🔗 [Sidewinder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/Sidewinder.py) - Creates mazes with a distinct horizontal bias
- 🔗 [Wilson](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/Wilson.py) - Loop-erased random walk algorithm for uniform spanning trees

---

## 🎯 Maze Solution Algorithms

Once mazes are generated, different algorithms are applied to solve them and analyze behavior under structural differences. This includes classical search techniques and reinforcement learning:

> **Note:** Algorithms marked with a * have been modified or developed by us.

- 🔗 [A-Star](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/AStar.py) - Heuristic-based pathfinding algorithm that combines uniform-cost search and greedy best-first search
- 🔗 [Breadth First Search (BFS)](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/BreadthFirstSearch.py) - Explores all nodes at the current depth before moving to the next level
- 🔗 [Depth First Search (DFS)](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/DepthFirstSearch.py) - Explores as far as possible along each branch before backtracking
- 🔗 [Hybrid Search*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/HybridSearch.py) - Custom algorithm combining BFS and DFS strategies for optimal exploration
- 🔗 [Random Walk](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/RandomWalk.py) - Stochastic approach that randomly selects moves until reaching the goal
- 🔗 [Hand on Wall](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/HandOnWall.py) - Follows walls to navigate through the maze using a simple rule-based approach
- 🔗 [Deep Q-Learning (DQN)*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/DeepQNetwork.ipynb) - Reinforcement learning approach using neural networks to learn optimal navigation policies

---

## 🎨 Maze Visualizations and Animations

To better understand the behavior of different generation and solution algorithms, we have included a collection of sample visualizations and animations.

You can download large (50x50) MP4 videos from the [Outputs folder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/tree/main/MazeAnimations/Outputs). Smaller 25x25 examples can be viewed interactively in the [animation.md](MazeAnimations/animation.md) file.

These examples demonstrate how mazes are generated and how solvers navigate through them.

---


## 📊 Data & Evaluation

All generated mazes are **sampled** and **evaluated** based on their:  
- Structural complexity  
- Solvability under different algorithms  
- Agent performance and behavior (classical vs. DQN)  

These analyses helped understand how maze structure affects exploration patterns and solution difficulty.