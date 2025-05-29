import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

class LoopHuntAndKillMaze:
    def __init__(self, width, height, loop_density = 0.01):
        self.maze_name = "Loop Hunt and Kill Algorithm"
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
        visited_cells = set()
        current_cell = self.start

        while True:
            visited_cells.add(current_cell)
            possible_neighbors = [n for n in self.graph.neighbors(current_cell) if n not in visited_cells]
            
            if possible_neighbors:
                next_cell = random.choice(possible_neighbors)
                self.maze.add_edge(current_cell, next_cell)
                self._update_grid(current_cell, next_cell)
                self.frames.append(self.grid.copy())
                current_cell = next_cell
            else:
                found = False
                for y in range(self.height):
                    for x in range(self.width):
                        if (x, y) not in visited_cells:
                            possible_neighbors = [n for n in self.graph.neighbors((x, y)) if n in visited_cells]
                            if possible_neighbors:
                                current_cell = (x, y)
                                next_cell = random.choice(possible_neighbors)
                                self.maze.add_edge(current_cell, next_cell)
                                self._update_grid(current_cell, next_cell)
                                self.frames.append(self.grid.copy())
                                visited_cells.add(current_cell)
                                found = True
                                break
                    if found:
                        break
                if not found:
                    break

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
                px1, py1 = prev[0] * 2

    def to_grid(self):
        return self.grid
    
    def to_graph(self):
        return self.maze