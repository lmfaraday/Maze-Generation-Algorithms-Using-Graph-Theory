import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

class LoopPrimMaze:
    def __init__(self, width, height, loop_density = 0.01):
        self.maze_name = "Loop Prim Algorithm"
        self.loop_density = loop_density
        self.width = width
        self.height = height
        self.graph = nx.grid_2d_graph(width, height)
        self.maze = nx.Graph()
        self.grid = np.ones((self.height * 2 + 1, self.width * 2 + 1))  
        self.frames = []
        self.start = (0, 0)
        self.end = (self.width - 1, self.height - 1)
        self._generate_maze(int(loop_density * (self.width * self.height) / 2))
    
    def _generate_maze(self, loop_amount):
        visited_cells = {self.start}
        wall_list = [(self.start, neighbor) for neighbor in self.graph.neighbors(self.start)]
        random.shuffle(wall_list)
        
        while wall_list:
            current_cell, next_cell = wall_list.pop()
            
            if next_cell not in visited_cells:
                visited_cells.add(next_cell)
                self.maze.add_edge(current_cell, next_cell)
                self._update_grid(current_cell, next_cell)
                self.frames.append(self.grid.copy())  

                for adjacent_cell in self.graph.neighbors(next_cell):
                    if adjacent_cell not in visited_cells:
                        wall_list.append((next_cell, adjacent_cell))
                        
                random.shuffle(wall_list)

        for _ in range(loop_amount):
            self._create_loop()
            
    def _create_loop(self):
        cell_list = list(self.maze.nodes())
        random.shuffle(cell_list)
        
        for cell in cell_list:
            connected_neighbors = list(self.maze.neighbors(cell))
            
            if len(connected_neighbors) < 4:
                possible_neighbors = list(self.graph.neighbors(cell))
                random.shuffle(possible_neighbors)
                
                for neighbor in possible_neighbors:
                    if neighbor not in connected_neighbors:
                        self.maze.add_edge(cell, neighbor)
                        self._update_grid(cell, neighbor)
                        self.frames.append(self.grid.copy())
                        return 
    
    def _update_grid(self, cell, neighbor):
        x1, y1 = cell
        x2, y2 = neighbor
        gx1, gy1 = x1 * 2 + 1, y1 * 2 + 1
        gx2, gy2 = x2 * 2 + 1, y2 * 2 + 1
        self.grid[gy1][gx1] = 0
        self.grid[gy2][gx2] = 0
        self.grid[(gy1 + gy2) // 2][(gx1 + gx2) // 2] = 0
    
    def draw(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.grid, cmap="binary", interpolation="nearest")
        
        sx, sy = self.start_cell
        ex, ey = self.end_cell
        gx1, gy1 = sx * 2 + 1, sy * 2 + 1
        gx2, gy2 = ex * 2 + 1, ey * 2 + 1
        plt.scatter(gx1, gy1, color="red", s=100, zorder=10, label="Start")
        plt.scatter(gx2, gy2, color="green", s=100, zorder=10, label="End")

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

        plt.scatter(self.start_cell[0], -self.start_cell[1], color="red", s=100, zorder=10, label="Start")
        plt.scatter(self.end_cell[0], -self.end_cell[1], color="green", s=100, zorder=10, label="End")

        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))        
        plt.xticks([]), plt.yticks([])
        plt.show()

    def draw_solution(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(self.grid, cmap="binary", interpolation="nearest")
        
        sx, sy = self.start_cell
        ex, ey = self.end_cell
        gx1, gy1 = sx * 2 + 1, sy * 2 + 1
        gx2, gy2 = ex * 2 + 1, ey * 2 + 1
        plt.scatter(gx1, gy1, color="red", s=100, zorder=10, label="Start")
        plt.scatter(gx2, gy2, color="green", s=100, zorder=10, label="End")

        solution_path = nx.shortest_path(self.maze, self.start_cell, self.end_cell)

        if solution_path:
            for i in range(1, len(solution_path)):
                prev = solution_path[i - 1]
                curr = solution_path[i]
                px1, py1 = prev[0] * 2 + 1, prev[1] * 2 + 1
                px2, py2 = curr[0] * 2 + 1, curr[1] * 2 + 1
                plt.plot([px1, px2], [py1, py2], color="green", linewidth=2, zorder=5)

        plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))        
        plt.xticks([]), plt.yticks([])
        plt.show()  

    def to_grid(self):
        return self.grid
    
    def to_graph(self):
        return self.maze