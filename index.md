📄 **Full Project Report:**  
Access the complete project report **[here](#)**.  
*(Note: The link will be updated once the final report is available.)*

---

💻 **Explore the Code & Results:**  
All source code and detailed visualizations are available on the  
[GitHub Repository](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory).  
Feel free to dive in and explore!

---

# Maze Generation and Solution with Graph Theory

📌 This is a comprehensive project developed as part of the **Industrial Engineering Graduation Project** at **Boğaziçi University**.

The project focuses on generating mazes of varying structural complexity using **graph-based algorithms**, and solving them through **classical** and **reinforcement learning** techniques in specific **Deep Q-Network (DQN)**. After generation and solution processes, the mazes are **sampled and analyzed** to understand how structural features affect solvability and agent behavior.

---

## 📂 Table of Contents

- [Maze Generation Algorithms](#maze-generation-algorithms)  
  - [Prim-Based](#prim-based)  
  - [Hunt and Kill-Based](#hunt-and-kill-based)  
  - [Other Algorithms](#other-algorithms)  
- [Maze Solution Algorithms](#maze-solution-algorithms)  

---

## Maze Generation Algorithms

Maze generation is the core of this project. All mazes are generated on **grid graphs**, where nodes represent cells and edges represent possible passages. The algorithms vary in their logic, ranging from randomized traversal to minimum spanning tree-based structures.

Generation algorithms included in this project, in specific:

> **Note:** Algorithms marked with a * have been modified or developed by us.

### Prim-Based

- 🔗 [Randomized Prim](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RandomizedPrim.py)  
- 🔗 [Depth First Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/DepthFirstPrim.py)  
- 🔗 [Initialized Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/InitializedPrim.py)  
- 🔗 [Loop Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/LoopPrim.py)  
- 🔗 [Stochastic Prim*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/StochasticPrim.py)  

### Hunt and Kill-Based

- 🔗 [Hunt and Kill](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/HuntAndKill.py)  
- 🔗 [Loop Hunt and Kill*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/LoopHuntAndKill.py)  

### Other Algorithms

- 🔗 [Aldous-Broder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/AldousBroder.py)  
- 🔗 [DFS](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/DFS.py)  
- 🔗 [Recursive Backtracker](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RecursiveBacktracker.py)  
- 🔗 [Randomized Kruskal](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/RandomizedKruskal.py)  
- 🔗 [Sidewinder](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/Sidewinder.py)  
- 🔗 [Wilson](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeGenerationAlgorithms/Wilson.py)  

---

## Maze Solution Algorithms

Once mazes are generated, different algorithms are applied to solve them and analyze behavior under structural differences. This includes classical search techniques and reinforcement learning:

> **Note:** Algorithms marked with a * have been modified or developed by us.

- 🔗 [A-Star](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/AStar.py)  
- 🔗 [Breadth First Search (BFS)](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/BreadthFirstSearch.py)  
- 🔗 [Depth First Search (DFS)](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/DepthFirstSearch.py)  
- 🔗 [Hybrid Search*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/HybridSearch.py)  
- 🔗 [Random Walk](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/RandomWalk.py)  
- 🔗 [Hand on Wall](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/HandOnWall.py)  
- 🔗 [Deep Q-Learning (DQN)*](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/blob/main/MazeSolutionAlgorithms/DeepQNetwork.ipynb)  

---

## Maze Visualizations and Animations

To better understand the behavior of different generation and solution algorithms, we have included a collection of sample visualizations and animations.

Explore these examples in the [MazeAnimations/Outputs](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/tree/main/MazeAnimations/Outputs) folder in the repository. They showcase how the mazes evolve during generation and how various solvers navigate through them.

---

## 📊 Data & Evaluation

All generated mazes are **sampled** and **evaluated** based on their:  
- Structural complexity  
- Solvability under different algorithms  
- Agent performance and behavior (classical vs. DQN)  

These analyses helped understand how maze structure affects exploration patterns and solution difficulty.