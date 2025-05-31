# Maze Generation Algorithms Using Graph Theory

📌 Developed as part of the **Industrial Engineering Graduation Project** at **Boğaziçi University**.

This project explores **maze generation** using graph algorithms and their **solution** through classical and reinforcement learning methods, particularly **Deep Q-Networks (DQN)**. Generated mazes are structurally sampled to evaluate how features like loops and dead-ends affect solvability and agent behavior.

---

## Maze Generation Algorithms

Mazes are generated on **graphs** using a range of algorithms—from spanning tree methods to random walks.

### Included Algorithms:
- **Prim Variants\***: Randomized, Depth-First, Initialized, Loop, Stochastic  
- **Hunt and Kill\***: With and without loops  
- **Others**: Aldous-Broder, DFS, Recursive Backtracker, Kruskal, Sidewinder, Wilson  

> Algorithms marked with \* are custom modifications.

---

## Maze Solution Algorithms

We applied both classical and learning-based methods:

- **Classical**: A*, BFS, DFS, Random Walk, Hand on Wall  
- **Custom**: Hybrid Search\* (BFS + DFS mix)  
- **RL-Based**: Deep Q-Network (DQN)\*

---

## Visualizations and Animations

We visualized both the generation and solution phases using animations.  
- 📁 Large videos: [`Outputs/`](https://github.com/lmfaraday/Maze-Generation-Algorithms-Using-Graph-Theory/tree/main/MazeAnimations/Outputs)  
- 🧭 Interactive examples: [`animation.md`](MazeAnimations/animation.md)

---

## Data & Evaluation

All mazes and solutions are **sampled** for analysis:

### Sampling Notebooks
- 📘 `MazeMetrics.ipynb`: Structural metrics (path length, branching, etc.)  
- 📘 `LoopMazeMetrics.ipynb`: Loop influence on complexity  
- 📘 `SolutionStatistics.ipynb`: Classical solver performance  
- 📘 `LoopSolutionStatistics.ipynb`: Solver behavior with loops  
- 🤖 `DQNStatistics.ipynb`: Learning curves, reward trends

---

### Key Results

- 🌀 Mazes **with loops** are generally **easier**, offering alternative paths.  
- 🧱 Mazes **with many short dead-ends** are **harder**, increasing backtracking.  
- 🔍 Classical solvers struggle in dense dead-end mazes.  
- 🧭 **Hybrid Search\*** adapts well across maze types.  
- ⚡ **DQN** learns **faster in longer, direct mazes**, benefiting from steady rewards.

---