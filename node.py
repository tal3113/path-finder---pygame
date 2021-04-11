from utils import *


# ----------------- Colors  ------------------ #
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
TURQUISE = (64, 224, 208)


# ----------------- Classes  ----------------- #
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * WIDTH_OF_NODE
        self.y = col * WIDTH_OF_NODE
        self.color = WHITE
        self.neighbors = []
        self.show_color = True

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUISE

    def is_path(self):
        return self.color == PURPLE

    def reset(self):
        self.color = WHITE
        self.show_color = True

    def make_closed(self):
        self.color = RED
        self.show_color = True

    def make_open(self):
        self.color = GREEN
        self.show_color = True

    def make_barrier(self):
        self.color = BLACK
        self.show_color = True

    def make_start(self):
        self.color = ORANGE
        self.show_color = True

    def make_end(self):
        self.color = TURQUISE
        self.show_color = True

    def make_path(self):
        self.color = PURPLE
        self.show_color = True

    def negate_show_color(self):
        self.show_color = not self.show_color

    def draw(self):
        if self.show_color:
            pygame.draw.rect(WINDOW, self.color,
                             (self.x, self.y, WIDTH_OF_NODE, WIDTH_OF_NODE))
        else:
            pygame.draw.rect(WINDOW, WHITE,
                             (self.x, self.y, WIDTH_OF_NODE, WIDTH_OF_NODE))

    def update_neighbors(self, grid):
        self.neighbors = []

        # DOWN
        if self.row < NUM_OF_ROWS - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < NUM_OF_ROWS - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
