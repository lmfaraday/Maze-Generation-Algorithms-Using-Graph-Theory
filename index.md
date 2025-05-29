---
title: Maze Generation and Solution with Graph Theory
---

📄 **You can access the full project report [here](#).**  
*(Link will be updated with the final report location.)*

# Maze Generation and Solution with Graph Theory

📌 This is a comprehensive project developed as part of the **Industrial Engineering Graduation Project** at **Boğaziçi University**.

The project focuses on generating mazes of varying structural complexity using **graph-based algorithms**, and solving them through **classical** and **reinforcement learning** techniques such as **Deep Q-Network (DQN)**. After generation and solution processes, the mazes are **sampled and analyzed** to understand how structural features affect solvability and agent behavior.

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

### Prim-Based

- 🔗 [Randomized Prim](MazeGenerationAlgorithms/RandomizedPrim.py)  
- 🔗 [Depth First Prim*](MazeGenerationAlgorithms/DepthFirstPrim.py)  
- 🔗 [Initialized Prim*](MazeGenerationAlgorithms/InitializedPrim.py)  
- 🔗 [Loop Prim*](MazeGenerationAlgorithms/LoopPrim.py)  
- 🔗 [Stochastic Prim*](MazeGenerationAlgorithms/StochasticPrim.py)

### Hunt and Kill-Based

- 🔗 [Hunt and Kill](MazeGenerationAlgorithms/HuntAndKill.py)  
- 🔗 [Loop Hunt and Kill*](MazeGenerationAlgorithms/LoopHuntAndKill.py)  

### Other Algorithms

- 🔗 [Aldous-Broder](MazeGenerationAlgorithms/AldousBroder.py)  
- 🔗 [DFS](MazeGenerationAlgorithms/DFS.py)  
- 🔗 [Recursive Backtracker](MazeGenerationAlgorithms/RecursiveBacktracker.py)  
- 🔗 [Randomized Kruskal](MazeGenerationAlgorithms/RandomizedKruskal.py)  
- 🔗 [Sidewinder](MazeGenerationAlgorithms/Sidewinder.py)  
- 🔗 [Wilson](MazeGenerationAlgorithms/Wilson.py)  

---

## Maze Solution Algorithms

Once mazes are generated, different algorithms are applied to solve them and analyze behavior under structural differences. This includes classical search techniques and reinforcement learning:

- 🔗 [A\*](MazeSolutionAlgorithms/AStar.py)  
- 🔗 [Breadth First Search (BFS)](MazeSolutionAlgorithms/BreadthFirstSearch.py)  
- 🔗 [Depth First Search (DFS)](MazeSolutionAlgorithms/DepthFirstSearch.py)  
- 🔗 [Hybrid Search*](MazeSolutionAlgorithms/HybridSearch.py)  
- 🔗 [Random Walk](MazeSolutionAlgorithms/RandomWalk.py)  
- 🔗 [Hand on Wall](MazeSolutionAlgorithms/HandOnWall.py)  
- 🔗 [Deep Q-Learning (DQN)*](MazeSolutionAlgorithms/DeepQNetwork.ipynb)  

---

## 📊 Data & Evaluation

All generated mazes are **sampled** and **evaluated** based on their:
- Structural complexity
- Solvability under different algorithms
- Agent performance and behavior (classical vs. DQN)

These analyses helped understand how maze structure affects exploration patterns and solution difficulty.

---

## 🔗 Access the Full Repository

You can access the full source code, visualizations, and result notebooks from the [GitHub Repository](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory).
