import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import random

class RandomWalkSolver:
    def __init__(self, maze):
        self.maze = maze.maze
        self.maze_name = maze.maze_name  
        self.grid = maze.grid  
        self.start = maze.start  
        self.end = maze.end  
        self.width = maze.width  
        self.height = maze.height  
        self.walk_frames = []
        self.visited = set()
        self.solution_path = self._solve()

    def _solve(self):
        current = self.start
        path = [current]
        visited = set()
        
        walk_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        walk_grid[self.grid == 1] = [0, 0, 0]
        walk_grid[self.grid == 0] = [1, 1, 1]
        
        while current != self.end:
            visited.add(current)
            
            walk_grid[current[1] * 2 + 1, current[0] * 2 + 1] = [0.0, 0.290, 0.678]
            if len(path) > 1:
                prev = path[-2]
                walk_grid[(current[1] + prev[1]) + 1, (current[0] + prev[0]) + 1] = [0.0, 0.290, 0.678]
            
            current_grid = walk_grid.copy()
            current_grid[current[1] * 2 + 1, current[0] * 2 + 1] = [1, 0, 0]  
            self.walk_frames.append(current_grid)
            
            neighbors = [n for n in self.maze.neighbors(current) if n not in visited]
            
            if neighbors:
                current = random.choice(neighbors)
                path.append(current)
            else:
                if len(path) > 1:
                    path.pop()
                    current = path[-1]
                else:
                    break  

        self.visited = visited
        
        solution_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        solution_grid[self.grid == 1] = [0, 0, 0]
        solution_grid[self.grid == 0] = [1, 1, 1]
        
        for node in path:
            solution_grid[node[1] * 2 + 1, node[0] * 2 + 1] = [0, 1, 0]  
        for i in range(1, len(path)):
            prev = path[i - 1]
            curr = path[i]
            solution_grid[(curr[1] + prev[1]) + 1, (curr[0] + prev[0]) + 1] = [0, 1, 0]  
        self.walk_frames.append(solution_grid)
        
        return path
    
    def animate(self, save=False):
        fig, ax = plt.subplots(figsize=(6, 6))
        cmap = plt.cm.binary
        im = ax.imshow(self.walk_frames[0], cmap=cmap, animated=True)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)
        
        def update(frame):
            im.set_array(frame)
            return [im]

        ani = animation.FuncAnimation(fig, update, frames=self.walk_frames, interval=50, repeat=False)
        
        if save or len(self.walk_frames) > 1000:
            print("Saving the animation...")
            ani.save(f"Outputs/Random Walk Solution of {self.maze_name}_{self.width}_{self.height}.mp4", 
                    writer="ffmpeg", bitrate=1000, 
                    fps=len(self.walk_frames) / (len(self.walk_frames) * 0.05))
            plt.close(fig)
        else:
            html_anim = HTML(ani.to_jshtml())
            plt.close(fig)
            return html_anim