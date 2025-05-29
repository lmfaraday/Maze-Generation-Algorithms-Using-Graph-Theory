import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

class DepthFirstPrimMaze:
    def __init__(self, width, height):
        self.maze_name = "Depth First Prim's Algorithm"
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
        visited_cells = {self.start}
        walls = [(self.start, neighbor) for neighbor in self.graph.neighbors(self.start)]
        depth_counter = 0
        max_depth = random.randint(self.width // 2, self.width)

        while walls:
            less_explored_walls = [
                (cell, neighbor) for cell, neighbor in walls
                if sum(1 for n in self.graph.neighbors(neighbor) if n in visited_cells) <= 1
            ]
            
            if less_explored_walls and depth_counter < max_depth:
                cell, neighbor = random.choice(less_explored_walls)
                depth_counter += 1
            else:
                cell, neighbor = random.choice(walls)
                depth_counter = 0
                max_depth = random.randint(self.width // 2, self.width)

            walls.remove((cell, neighbor))

            if neighbor not in visited_cells:
                visited_cells.add(neighbor)
                self.maze.add_edge(cell, neighbor)
                self._update_grid(cell, neighbor)
                self.frames.append(self.grid.copy())

                for next_neighbor in self.graph.neighbors(neighbor):
                    if next_neighbor not in visited_cells:
                        walls.append((neighbor, next_neighbor))

    def _update_grid(self, cell, neighbor):
        x1, y1 = cell
        x2, y2 = neighbor
        grid_x1, grid_y1 = x1 * 2 + 1, y1 * 2 + 1
        grid_x2, grid_y2 = x2 * 2 + 1, y2 * 2 + 1
        self.grid[grid_y1][grid_x1] = 0
        self.grid[grid_y2][grid_x2] = 0
        self.grid[(grid_y1 + grid_y2) // 2][(grid_x1 + grid_x2) // 2] = 0
    
    def draw(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.grid, cmap="binary", interpolation="nearest")
        
        start_x, start_y = self.start
        end_x, end_y = self.end
        grid_start_x, grid_start_y = start_x * 2 + 1, start_y * 2 + 1
        grid_end_x, grid_end_y = end_x * 2 + 1, end_y * 2 + 1
        plt.scatter(grid_start_x, grid_start_y, color="red", s=100, zorder=10, label="Start")
        plt.scatter(grid_end_x, grid_end_y, color="green", s=100, zorder=10, label="End")

        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))        
        plt.xticks([]), plt.yticks([])
        plt.show()
    
    def animate_maze(self, save=False):
        fig, ax = plt.subplots(figsize=(6, 6))

        cmap = plt.cm.binary
        im = ax.imshow(self.frames[0], cmap=cmap, animated=True)

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_frame_on(False)

        def update(frame):
            im.set_array(frame)
            return [im]

        ani = animation.FuncAnimation(fig, update, frames=self.frames, interval=50, repeat=False)

        if save or len(self.frames) > 1000:
            print("Saving the animation...")
            ani.save(f"Outputs/Generation of {self.maze_name}{self.width}_{self.height}.mp4", writer="ffmpeg", bitrate=1000, fps=len(self.frames) / (len(self.frames) * 0.05))
            plt.close(fig)    

        else:
            html_anim = HTML(ani.to_jshtml())
            plt.close(fig)
            return html_anim
    
    def visualize_maze_as_graph(self):
        plt.figure(figsize=(6, 6))
        pos = {(x, y): (x, -y) for x, y in self.graph.nodes()}  
        nx.draw(self.maze, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='black')

        plt.scatter(self.start[0], -self.start[1], color="red", s=100, zorder=10, label="Start")
        plt.scatter(self.end[0], -self.end[1], color="green", s=100, zorder=10, label="End")

        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))        
        plt.xticks([]), plt.yticks([])
        plt.show()

    def draw_solution(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.grid, cmap="binary", interpolation="nearest")
        
        start_x, start_y = self.start
        end_x, end_y = self.end
        grid_start_x, grid_start_y = start_x * 2 + 1, start_y * 2 + 1
        grid_end_x, grid_end_y = end_x * 2 + 1, end_y * 2 + 1
        plt.scatter(grid_start_x, grid_start_y, color="red", s=100, zorder=10, label="Start")
        plt.scatter(grid_end_x, grid_end_y, color="green", s=100, zorder=10, label="End")

        solution_path = nx.shortest_path(self.maze, self.start, self.end)

        if solution_path:
            for i in range(1, len(solution_path)):
                prev = solution_path[i - 1]
                curr = solution_path[i]
                prev_x, prev_y = prev[0] * 2 + 1, prev[1] * 2 + 1
                curr_x, curr_y = curr[0] * 2 + 1, curr[1] * 2 + 1
                plt.plot([prev_x, curr_x], [prev_y, curr_y], color="green", linewidth=2, zorder=5)

        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))        
        plt.xticks([]), plt.yticks([])
        plt.show()   

    def to_grid(self):
        return self.grid
    
    def to_graph(self):
        return self.maze
