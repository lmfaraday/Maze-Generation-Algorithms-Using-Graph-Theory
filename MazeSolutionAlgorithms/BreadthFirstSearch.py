import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from collections import deque

class BFSSolver:
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
        queue = deque([(self.start, [self.start])])  
        visited = set()
        search_grid = np.zeros((self.height * 2 + 1, self.width * 2 + 1, 3))
        search_grid[self.grid == 1] = [0, 0, 0]  
        search_grid[self.grid == 0] = [1, 1, 1]       
           
        while queue:
            current, path = queue.popleft()
            
            if current == self.end:
                search_grid[current[1] * 2 + 1, current[0] * 2 + 1] = [0.302, 0.486, 0.486]
                for i in range(1, len(path)):
                    prev = path[i - 1]
                    curr = path[i]
                    search_grid[(curr[1] + prev[1]) + 1, (curr[0] + prev[0]) + 1] = [0.302, 0.486, 0.486]
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
                
                self.visited = visited
                return path

            if current in visited:
                continue
            visited.add(current)
            
            search_grid[current[1] * 2 + 1, current[0] * 2 + 1] = [0.302, 0.486, 0.486]
            if len(path) > 1:
                prev = path[-2]
                search_grid[(current[1] + prev[1]) + 1, (current[0] + prev[0]) + 1] = [0.302, 0.486, 0.486]
            self.bfs_frames.append(search_grid.copy())

            for neighbor in self.maze.neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        
        self.visited = visited
        return []
    
    def animate(self, save=False):
        fig, ax = plt.subplots(figsize=(6, 6))

        cmap = plt.cm.binary
        im = ax.imshow(self.bfs_frames[0], cmap=cmap, animated=True)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        def update(frame):
            if frame.ndim == 3:  
                im.set_array(frame)
            else:  
                im.set_array(frame)
                im.set_cmap(cmap)
            return [im]

        ani = animation.FuncAnimation(fig, update, frames=self.bfs_frames, interval=50, repeat=False)
        
        if save or len(self.bfs_frames) > 1000:
            print("Saving the animation...")
            ani.save(f"Outputs/BFS Solution of {self.maze_name}_{self.width}_{self.height}.mp4", writer="ffmpeg", bitrate=1000, fps=len(self.bfs_frames) / (len(self.bfs_frames) * 0.05))  
            plt.close(fig)
        else:
            html_anim = HTML(ani.to_jshtml())
            plt.close(fig)  
            return html_anim