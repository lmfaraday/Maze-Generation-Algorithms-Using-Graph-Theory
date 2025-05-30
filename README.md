# Maze Generation Algorithms Using Graph Theory


📌 This project was developed as part of the **Industrial Engineering Graduation Project** at **Boğaziçi University**.

It focuses on generating mazes of varying structural complexity using **graph-based algorithms**, and solving them via **classical** and **reinforcement learning** techniques, specifically with **Deep Q-Networks (DQN)**. After generation and solution, mazes are **sampled and analyzed** to understand how structural features affect solvability and agent behavior.

---

## Maze Generation Algorithms

Mazes are generated on grid graphs where nodes represent cells and edges represent passages. Algorithms range from randomized traversals to minimum spanning tree methods.

### Examples Include:  
- Prim-Based variations (including custom modifications)*  
- Hunt and Kill and Loop Hunt and Kill*  
- Aldous-Broder, Recursive Backtracker, Randomized Kruskal, Sidewinder, Wilson

(* indicates modified or developed by us)

---

## Maze Solution Algorithms

Solvers include classical search and reinforcement learning:

- A-Star, BFS, DFS  
- Hybrid Search* (custom BFS + DFS)  
- Random Walk, Hand on Wall  
- Deep Q-Learning (DQN)*

---

## Visualizations and Animations

Sample visualizations and videos illustrate maze generation and solution processes.  
Large videos available in the Outputs folder, smaller interactive examples in the animation.md file.

---

## Data & Evaluation

Generated mazes are sampled and evaluated by:  
- Structural complexity  
- Solvability under various algorithms  
- Agent performance and behavior (classical vs. DQN)

