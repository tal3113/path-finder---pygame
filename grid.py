from node import Node
from utils import *






# ----------------- Classes  ----------------- #
class Grid():
    def __init__(self):
        self.grid = self.make_grid()

    def get_grid(self):
        return self.grid

    def make_grid(self):
        grid = []
        for i in range(NUM_OF_ROWS):
            grid.append([])
            for j in range(NUM_OF_ROWS):
                node = Node(i, j)
                grid[i].append(node)
        return grid

    def draw_grid(self):
        for i in range(NUM_OF_ROWS):
            pygame.draw.line(WINDOW, GREY, (0, i * WIDTH_OF_NODE),
                             (WIDTH, i * WIDTH_OF_NODE))
        for j in range(NUM_OF_ROWS):
            pygame.draw.line(WINDOW, GREY, (j * WIDTH_OF_NODE, 0),
                             (j * WIDTH_OF_NODE, WIDTH))
