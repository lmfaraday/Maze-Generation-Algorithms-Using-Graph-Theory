import heapq
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

class AStarSolver:
    def __init__(self, maze):
        self.maze = maze.maze
        self.maze_name = maze.maze_name  
        self.grid = maze.grid  
        self.start = maze.start  
        self.end = maze.end  
        self.width = maze.width  
        self.height = maze.height  
        self.search_frames = []
        self.visited = set()
        self.solution_path = self._solve()

    def _heuristic(self, a, b):
        return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])

    def _solve(self):
        frontier = []
        heapq.heappush(frontier, (0, self.start))  
        came_from = {self.start: None}
        cost_so_far = {self.start: 0}

        search_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        search_grid[self.grid == 1] = [0, 0, 0]  
        search_grid[self.grid == 0] = [1, 1, 1]  
        
        while frontier:
            _, current = heapq.heappop(frontier)
            self.visited.add(current)

            x, y = current
            search_grid[y * 2 + 1, x * 2 + 1] = [0.3176, 0.7098, 0.8314]

            if came_from[current] is not None:
                prev_x, prev_y = came_from[current]
                edge_x = (x + prev_x) + 1
                edge_y = (y + prev_y) + 1
                search_grid[edge_y, edge_x] = [0.3176, 0.7098, 0.8314]   

            self.search_frames.append(search_grid.copy())

            if current == self.end:
                break

            for neighbor in self.maze.neighbors(current):
                new_cost = cost_so_far[current] + 1  
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self._heuristic(neighbor, self.end)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current
        
        solution_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        solution_grid[self.grid == 1] = [0, 0, 0]  
        solution_grid[self.grid == 0] = [1, 1, 1]  

        path = self._reconstruct_path(came_from)
        for i in range(len(path) - 1):
            x, y = path[i]
            solution_grid[y * 2 + 1, x * 2 + 1] = [0, 1, 0]  
            
            next_x, next_y = path[i + 1]
            edge_x = (x + next_x) + 1
            edge_y = (y + next_y) + 1
            solution_grid[edge_y, edge_x] = [0, 1, 0] 

        end_x, end_y = self.end
        solution_grid[end_y * 2 + 1, end_x * 2 + 1] = [0, 1, 0] 

        self.search_frames.append(solution_grid)  
        return self.visited
    
    def _reconstruct_path(self, came_from):
        current = self.end
        path = []
        while current != self.start:
            path.append(current)
            current = came_from.get(current, self.start)  
        path.append(self.start)
        path.reverse()
        return path

    def animate(self, save=False):
        fig, ax = plt.subplots(figsize=(6, 6))

        cmap = plt.cm.binary
        im = ax.imshow(self.search_frames[0], cmap=cmap, animated=True)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        def update(frame):
            im.set_array(frame)
            return [im]

        ani = animation.FuncAnimation(fig, update, frames=self.search_frames, interval=50, repeat=False)

        if save or len(self.search_frames) > 1000:
            print("Saving the animation...")
            ani.save(f"Outputs/AStar Solution of {self.maze_name}_{self.width}_{self.height}.mp4", 
                     writer="ffmpeg", bitrate=1000, fps=len(self.search_frames) / (len(self.search_frames) * 0.05))
            plt.close(fig)
        else:
            html_anim = HTML(ani.to_jshtml())
            plt.close(fig)
            return html_anim