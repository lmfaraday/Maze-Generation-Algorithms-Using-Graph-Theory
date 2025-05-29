import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

class RandomizedPrimMaze:
    def __init__(self, width, height):
        self.maze_name = "Randomized Prim's Algorithm"
        self.width = width
        self.height = height
        self.graph = nx.grid_2d_graph(width, height)
        self.maze = nx.Graph()
        self.grid = np.ones((self.height * 2 + 1, self.width * 2 + 1))
        self.frames = []
        self.start = (0, 0)
        self.end = (self.width - 1, self.height - 1)
        self._generate_maze()
    
    def _generate_maze(self):
        visited = {self.start}
        walls = [(self.start, neighbor) for neighbor in self.graph.neighbors(self.start)]
        random.shuffle(walls)
        
        while walls:
            cell, neighbor = walls.pop()
            if neighbor not in visited:
                visited.add(neighbor)
                self.maze.add_edge(cell, neighbor)

                self._update_grid(cell, neighbor)
                self.frames.append(self.grid.copy())

                for next_neighbor in self.graph.neighbors(neighbor):
                    if next_neighbor not in visited:
                        walls.append((neighbor, next_neighbor))
                random.shuffle(walls)
    
    def _update_grid(self, cell, neighbor):
        x1, y1 = cell
        x2, y2 = neighbor
        grid_x1, grid_y1 = x1 * 2 + 1, y1 * 2 + 1
        grid_x2, grid_y2 = x2 * 2 + 1, y2 * 2 + 1
        self.grid[grid_y1][grid_x1] = 0
        self.grid[grid_y2][grid_x2] = 0
        self.grid[(grid_y1 + grid_y2) // 2][(grid_x1 + grid_x2) // 2] = 0
    
    def to_grid(self):
        return self.grid
    
    def to_graph(self):
        return self.maze

class HybridBFSDFS:
    def __init__(self, maze):
        self.maze = maze.maze
        self.maze_name = maze.maze_name
        self.grid = maze.grid
        self.start = maze.start
        self.end = maze.end
        self.width = maze.width
        self.height = maze.height
        self.bfs_frames = []
        self.visited = set()
        self.solution_path = self._solve()

    def _solve(self):
        total_cells = self.width * self.height
        bfs_threshold = total_cells // 3
        
        queue = deque([(self.start, [self.start])])
        visited = set()
        search_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        search_grid[self.grid == 1] = [0, 0, 0]
        search_grid[self.grid == 0] = [1, 1, 1]
        
        while queue and len(visited) < bfs_threshold:
            current, path = queue.popleft()
            if current == self.end:
                return self._mark_solution(search_grid, path)
            if current in visited:
                continue
            visited.add(current)
            self.visited.add(current)
            search_grid[current[1] * 2 + 1, current[0] * 2 + 1] = [0.302, 0.486, 0.486]
            if len(path) > 1:
                prev = path[-2]
                search_grid[(current[1] + prev[1]) + 1, (current[0] + prev[0]) + 1] = [0.302, 0.486, 0.486]
            self.bfs_frames.append(search_grid.copy())

            neighbors = []
            for neighbor in self.maze.neighbors(current):
                if neighbor not in visited:
                    manhattan_dist = abs(neighbor[0] - self.end[0]) + abs(neighbor[1] - self.end[1])
                    neighbors.append((manhattan_dist, neighbor, path + [neighbor]))
            neighbors.sort(key=lambda x: x[0])
            for _, neighbor, new_path in neighbors:
                queue.append((neighbor, new_path))
        
        stack = [(current, path) for current, path in queue]
        while stack:
            current, path = stack.pop()
            if current == self.end:
                return self._mark_solution(search_grid, path)
            if current in visited:
                continue
            visited.add(current)
            self.visited.add(current)
            search_grid[current[1] * 2 + 1, current[0] * 2 + 1] = [0.396, 0.804, 0.929]
            if len(path) > 1:
                prev = path[-2]
                search_grid[(current[1] + prev[1]) + 1, (current[0] + prev[0]) + 1] = [0.396, 0.804, 0.929]
            self.bfs_frames.append(search_grid.copy())

            neighbors = []
            for neighbor in self.maze.neighbors(current):
                if neighbor not in visited:
                    manhattan_dist = abs(neighbor[0] - self.end[0]) + abs(neighbor[1] - self.end[1])
                    neighbors.append((manhattan_dist, neighbor, path + [neighbor]))
            neighbors.sort(key=lambda x: x[0], reverse=True)
            for _, neighbor, new_path in neighbors:
                stack.append((neighbor, new_path))
        
        return None

    def _mark_solution(self, search_grid, path):
        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            search_grid[curr[1] * 2 + 1, curr[0] * 2 + 1] = [0, 0.6, 0.9]
            search_grid[(curr[1] + prev[1]) + 1, (curr[0] + prev[0]) + 1] = [0, 0.6, 0.9]
        self.bfs_frames.append(search_grid.copy())

        solution_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        solution_grid[self.grid == 1] = [0, 0, 0]
        solution_grid[self.grid == 0] = [1, 1, 1]

        for node in path:
            solution_grid[node[1] * 2 + 1, node[0] * 2 + 1] = [0, 1, 0]
        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            solution_grid[(curr[1] + prev[1]) + 1, (curr[0] + prev[0]) + 1] = [0, 1, 0]
        self.bfs_frames.append(solution_grid)

        return None

def animate_side_by_side(maze_obj, solver_obj, save=False):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Add descriptive titles with custom styling
    ax1.set_title("Maze Generation", fontsize=14, pad=15, fontweight='bold')
    ax2.set_title("Finding the Solution", fontsize=14, pad=15, fontweight='bold')
    
    # Initialize images
    im1 = ax1.imshow(maze_obj.frames[0], cmap="binary", animated=True)
    im2 = ax2.imshow(solver_obj.bfs_frames[0], animated=True)
    
    # Clean up axes
    ax1.axis('off')
    ax2.axis('off')
    
    def update(frame):
        gen_idx = min(frame, len(maze_obj.frames)-1)
        sol_idx = min(frame, len(solver_obj.bfs_frames)-1)
        
        im1.set_array(maze_obj.frames[gen_idx])
        im2.set_array(solver_obj.bfs_frames[sol_idx])
        
        
        return im1, im2

    total_frames = max(len(maze_obj.frames), len(solver_obj.bfs_frames))
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=total_frames, 
        interval=50, 
        blit=True, 
        repeat=False
    )

    if save:
        print(f"Saving animation to Outputs/SideBySide_{maze_obj.maze_name}_{maze_obj.width}x{maze_obj.height}.mp4")
        ani.save(
            f"Outputs/SideBySide_{maze_obj.maze_name}_{maze_obj.width}x{maze_obj.height}.mp4",
            writer="ffmpeg",
            fps=20,
            dpi=100,
            bitrate=2000
        )
        plt.close(fig)
    else:
        plt.show()

if __name__ == "__main__":
    width, height = 20, 20
    maze = RandomizedPrimMaze(width, height)
    solver = HybridBFSDFS(maze)
    animate_side_by_side(maze, solver, save=True)
