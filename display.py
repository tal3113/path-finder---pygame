from algorithm import Algorithm
from grid import Grid
from utils import WIDTH_OF_NODE, WINDOW, pygame, WHITE


# ----------------- Classes  ----------------- #
class Display():
    def __init__(self):
        self.grid = Grid()
        self.current_node = None
        self.start = None
        self.end = None
        self.algorithm = None
        self.started = False
        self.algorithm_shows = False
        self.before_algorithm = True

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def draw(self):
        WINDOW.fill(WHITE)
        for row in self.grid.get_grid():
            for node in row:
                node.draw()
        self.grid.draw_grid()
        pygame.display.update()

    def show_result(self):
        for row in self.grid.get_grid():
            for node in row:
                if node.is_open() or node.is_closed():
                    node.negate_show_color()

        self.draw()

    def reset_show_algorithm(self):
        for row in self.grid.get_grid():
            for node in row:
                if node.is_open() or node.is_closed() or node.is_path():
                    node.reset()
        self.draw()

    def get_clicked_node(self, pos):
        y, x = pos
        row = y // WIDTH_OF_NODE
        col = x // WIDTH_OF_NODE
        self.current_node = self.grid.get_grid()[row][col]

    def left_mouse_click(self):
        if not self.start and self.current_node != self.end:
            self.start = self.current_node
            self.start.make_start()

        elif not self.end and self.current_node != self.start:
            self.end = self.current_node
            self.end.make_end()

        elif self.current_node != self.start and self.current_node != self.end:
            self.current_node.make_barrier()

    def right_mouse_click(self):
        self.current_node.reset()
        if self.current_node == self.start:
            self.start = None

        elif self.current_node == self.end:
            self.end = None

    def space_key_down(self):
        if self.start and self.end:
            self.algorithm = Algorithm(self.start, self.end)
            grid = self.grid.get_grid()
            for row in grid:
                for node in row:
                    node.update_neighbors(grid)

            if not self.before_algorithm:
                self.reset_show_algorithm()

            self.started = True
            self.algorithm.run_algorithm(
                lambda: self.draw(), self.start, self.end, self.grid.get_grid())
            self.before_algorithm = False
            self.started = False
            self.algorithm_shows = True

    def get_started(self):
        return self.started

    def reset_display(self):
        self.__init__()

    def path_key_down(self):
        if self.algorithm_shows:
            self.show_result()
            self.algorithm_shows = False

    def all_key_down(self):
        if not self.before_algorithm and not self.algorithm_shows:
            self.show_result()
            self.algorithm_shows = True
